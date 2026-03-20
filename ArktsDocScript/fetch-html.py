"""Huawei developer docs crawler.

This script uses Playwright to wait for a page to finish rendering before
exporting the final HTML. It crawls only an explicit whitelist of URLs loaded
from a text file, so the crawl stays bounded and easy to maintain.

Usage:
	python fetch-html.py --targets-file ./huawei_targets.txt --output-dir ./huawei_docs

Dependencies:
	pip install playwright
	playwright install chromium
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
import time
import shutil
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urljoin, urlparse, urlunparse

from playwright.async_api import TimeoutError as PlaywrightTimeoutError
from playwright.async_api import async_playwright


DEFAULT_TARGETS_FILE = "./huawei_targets.txt"
DEFAULT_OUTPUT_DIR = "./huawei_docs"
DEFAULT_USER_AGENT = (
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
	"(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
DEFAULT_STABLE_MS = 350
DEFAULT_PAGE_TIMEOUT_MS = 20_000
DEFAULT_MAX_PAGES = 200
DEFAULT_SCROLL_PASSES = 4
DEFAULT_SCROLL_WAIT_MS = 80
DEFAULT_RENDER_POLL_MS = 100
DEFAULT_CONCURRENCY = 5
FAST_MODE_MIN_CONCURRENCY = 6
FAST_MODE_STABLE_MS = 150
FAST_MODE_SCROLL_PASSES = 2
FAST_MODE_SCROLL_WAIT_MS = 40
FAST_MODE_RENDER_POLL_MS = 50
BLOCKED_RESOURCE_TYPES = {"image", "media", "font"}

TRACKING_QUERY_KEYS = {
	"from",
	"spm",
	"utm_source",
	"utm_medium",
	"utm_campaign",
	"utm_term",
	"utm_content",
	"share",
}

LINK_SELECTORS = [
	"main a[href]",
	"article a[href]",
	"nav a[href]",
	"aside a[href]",
	"[role='navigation'] a[href]",
	"[role='tree'] a[href]",
	"[class*='toc'] a[href]",
	"[class*='nav'] a[href]",
	"[class*='menu'] a[href]",
	"[class*='sidebar'] a[href]",
]


@dataclass
class CrawlRecord:
	url: str
	final_url: str
	title: str
	html_path: str
	discovered_from: str | None
	outbound_links: int
	status: str
	fetched_at: float


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		description=(
			"Crawl Huawei developer docs from an explicit target URL whitelist."
		)
	)
	parser.add_argument("--targets-file", default=DEFAULT_TARGETS_FILE)
	parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR)
	parser.add_argument("--max-pages", type=int, default=DEFAULT_MAX_PAGES)
	parser.add_argument("--stable-ms", type=int, default=DEFAULT_STABLE_MS)
	parser.add_argument("--scroll-passes", type=int, default=DEFAULT_SCROLL_PASSES)
	parser.add_argument("--scroll-wait-ms", type=int, default=DEFAULT_SCROLL_WAIT_MS)
	parser.add_argument("--render-poll-ms", type=int, default=DEFAULT_RENDER_POLL_MS)
	parser.add_argument("--concurrency", type=int, default=DEFAULT_CONCURRENCY)
	parser.add_argument("--page-timeout-ms", type=int, default=DEFAULT_PAGE_TIMEOUT_MS)
	parser.add_argument(
		"--fast-mode",
		action="store_true",
		help="Enable 极速模式: higher concurrency and shorter waits for faster bulk crawling.",
	)
	parser.add_argument(
		"--headful",
		action="store_true",
		help="Run a visible browser window for debugging.",
	)
	return parser.parse_args()


def log(message: str) -> None:
	print(message, file=sys.stdout, flush=True)


def ensure_output_dirs(output_dir: Path) -> tuple[Path, Path]:
	html_dir = output_dir / "pages"
	meta_dir = output_dir / "meta"
	if html_dir.exists():
		shutil.rmtree(html_dir)
	if meta_dir.exists():
		shutil.rmtree(meta_dir)
	html_dir.mkdir(parents=True, exist_ok=True)
	meta_dir.mkdir(parents=True, exist_ok=True)
	return html_dir, meta_dir


def canonicalize_url(raw_url: str, base_url: str | None = None) -> str | None:
	if not raw_url:
		return None

	candidate = urljoin(base_url, raw_url) if base_url else raw_url
	parsed = urlparse(candidate)
	if parsed.scheme not in {"http", "https"}:
		return None

	query_items = [
		(key, value)
		for key, value in parse_qsl(parsed.query, keep_blank_values=True)
		if key.lower() not in TRACKING_QUERY_KEYS
	]
	normalized_query = urlencode(query_items, doseq=True)
	normalized_path = re.sub(r"/{2,}", "/", parsed.path or "/")
	if normalized_path != "/" and normalized_path.endswith("/"):
		normalized_path = normalized_path.rstrip("/")

	normalized = parsed._replace(
		path=normalized_path,
		params="",
		query=normalized_query,
		fragment="",
	)
	return urlunparse(normalized)


def is_huawei_doc_url(url: str) -> bool:
	parsed = urlparse(url)
	if parsed.scheme not in {"http", "https"}:
		return False
	if not parsed.netloc.endswith("huawei.com"):
		return False
	if not parsed.path.startswith("/consumer/cn/doc/harmonyos-references/"):
		return False
	if re.search(r"\.(?:png|jpe?g|gif|webp|svg|css|js|ico|pdf|zip|rar|7z)$", parsed.path, re.I):
		return False
	return True


def slug_from_index(index: int) -> str:
	return f"{index:03d}.html"


def load_target_urls(targets_file: Path) -> list[str]:
	if not targets_file.exists():
		raise FileNotFoundError(f"targets file not found: {targets_file}")

	target_urls: list[str] = []
	seen: set[str] = set()
	for raw_line in targets_file.read_text(encoding="utf-8").splitlines():
		line = raw_line.strip()
		if not line or line.startswith("#"):
			continue
		normalized = canonicalize_url(line)
		if not normalized or normalized in seen:
			continue
		seen.add(normalized)
		target_urls.append(normalized)
	return target_urls


async def install_render_watchers(page) -> None:
	await page.evaluate(
		"""
		() => {
		  if (!window.__crawlerDomStateInstalled) {
			window.__crawlerDomState = { lastMutationAt: performance.now() };
			const observer = new MutationObserver(() => {
			  window.__crawlerDomState.lastMutationAt = performance.now();
			});
			observer.observe(document.documentElement, {
			  childList: true,
			  subtree: true,
			});
			window.__crawlerDomStateInstalled = true;
		  }
		}
		"""
	)


async def wait_for_true_render(page, stable_ms: int, timeout_ms: int, poll_ms: int) -> dict:
	deadline = time.monotonic() + timeout_ms / 1000
	last_snapshot: dict = {}

	while time.monotonic() < deadline:
		last_snapshot = await page.evaluate(
			"""
			() => {
			  const domState = window.__crawlerDomState || { lastMutationAt: performance.now() };
			  const body = document.body;

			  return {
				readyState: document.readyState,
				msSinceMutation: performance.now() - domState.lastMutationAt,
				title: document.title || '',
				bodyPresent: Boolean(body),
			  };
			}
			"""
		)

		if (
			last_snapshot.get("readyState") in {"interactive", "complete"}
			and last_snapshot.get("msSinceMutation", 0) >= stable_ms
			and last_snapshot.get("bodyPresent", False)
		):
			return last_snapshot
		await page.wait_for_timeout(poll_ms)

	return last_snapshot


async def auto_scroll(page, max_passes: int, wait_ms: int) -> None:
	viewport_height = await page.evaluate(
		"() => window.innerHeight || document.documentElement.clientHeight || 0"
	)
	current_height = await page.evaluate(
		"() => Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0)"
	)
	if viewport_height and current_height <= int(viewport_height * 1.2):
		return

	previous_height = -1
	for _ in range(max_passes):
		current_height = await page.evaluate(
			"() => Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0)"
		)
		if current_height == previous_height:
			break
		previous_height = current_height
		await page.evaluate("() => window.scrollTo(0, document.documentElement.scrollHeight)")
		await page.wait_for_timeout(wait_ms)
	await page.evaluate("() => window.scrollTo(0, 0)")


async def extract_links(page, current_url: str) -> list[str]:
	links = await page.evaluate(
		r"""
		(selectors) => {
		  const collected = [];
		  const seen = new Set();

		  const pushLink = (anchor) => {
			const href = anchor.href || '';
			if (!href || seen.has(href)) {
			  return;
			}
			seen.add(href);
			collected.push({
			  href,
			  text: (anchor.textContent || '').replace(/\s+/g, ' ').trim(),
			});
		  };

		  let anchors = [];
		  for (const selector of selectors) {
			anchors = anchors.concat(Array.from(document.querySelectorAll(selector)));
		  }

		  if (anchors.length === 0) {
			anchors = Array.from(document.querySelectorAll('a[href]'));
		  }

		  for (const anchor of anchors) {
			pushLink(anchor);
		  }

		  return collected;
		}
		""",
		LINK_SELECTORS,
	)

	normalized: list[str] = []
	seen: set[str] = set()
	for item in links:
		candidate = canonicalize_url(item.get("href", ""), base_url=current_url)
		if not candidate or candidate in seen:
			continue
		seen.add(candidate)
		normalized.append(candidate)
	return normalized


async def block_unneeded_resources(route) -> None:
	if route.request.resource_type in BLOCKED_RESOURCE_TYPES:
		await route.abort()
		return
	await route.continue_()


async def crawl_docs(
	targets_file: Path,
	output_dir: Path,
	max_pages: int,
	stable_ms: int,
	scroll_passes: int,
	scroll_wait_ms: int,
	render_poll_ms: int,
	concurrency: int,
	page_timeout_ms: int,
	headful: bool,
	fast_mode: bool,
) -> None:
	html_dir, meta_dir = ensure_output_dirs(output_dir)
	manifest_path = meta_dir / "manifest.jsonl"
	urls_path = meta_dir / "discovered_urls.txt"

	target_urls = load_target_urls(targets_file)
	if not target_urls:
		raise ValueError(f"no valid target urls found in {targets_file}")

	selected_urls = target_urls[:max_pages]
	if not selected_urls:
		raise ValueError(f"no target urls selected from {targets_file}")

	async with async_playwright() as playwright:
		log(f"[crawl] launching browser for {len(selected_urls)} target urls")
		browser = await playwright.chromium.launch(headless=not headful)
		context = await browser.new_context(
			locale="zh-CN",
			user_agent=DEFAULT_USER_AGENT,
			viewport={"width": 1440, "height": 1600},
		)
		await context.route("**/*", block_unneeded_resources)
		await context.add_init_script(
			"window.__crawlerState = window.__crawlerState || { pendingRequests: 0 };"
		)
		if fast_mode:
			concurrency = max(concurrency, FAST_MODE_MIN_CONCURRENCY)
			stable_ms = min(stable_ms, FAST_MODE_STABLE_MS)
			scroll_passes = min(scroll_passes, FAST_MODE_SCROLL_PASSES)
			scroll_wait_ms = min(scroll_wait_ms, FAST_MODE_SCROLL_WAIT_MS)
			render_poll_ms = min(render_poll_ms, FAST_MODE_RENDER_POLL_MS)

		concurrency = max(1, concurrency)
		semaphore = asyncio.Semaphore(concurrency)

		try:
			log(
				f"[crawl] max_pages={max_pages}, stable_ms={stable_ms}, "
				f"concurrency={concurrency}, fast_mode={fast_mode}"
			)
			log(f"[crawl] output_dir={output_dir}")

			async def fetch_target(index: int, current_url: str) -> CrawlRecord:
				async with semaphore:
					page = await context.new_page()
					html_name = slug_from_index(index)
					html_path = html_dir / html_name
					final_url = current_url
					title = ""
					outbound_links: list[str] = []
					status = "ok"

					try:
						log(f"[crawl] fetching index={index} url={current_url}")
						log("[crawl] step=navigation wait_until=commit")
						try:
							await page.goto(current_url, wait_until="commit", timeout=page_timeout_ms)
						except PlaywrightTimeoutError:
							log("[crawl] navigation commit timeout, continuing with current page state")

						log("[crawl] step=post-navigation url=" + page.url)
						await install_render_watchers(page)

						try:
							log("[crawl] step=wait domcontentloaded")
							await page.wait_for_load_state("domcontentloaded", timeout=min(page_timeout_ms, 10_000))
						except PlaywrightTimeoutError:
							log("[crawl] domcontentloaded timeout, continuing")

						log("[crawl] step=auto-scroll")
						await auto_scroll(page, max_passes=scroll_passes, wait_ms=scroll_wait_ms)
						log("[crawl] step=stability-check")
						await wait_for_true_render(
							page,
							stable_ms=stable_ms,
							timeout_ms=page_timeout_ms,
							poll_ms=render_poll_ms,
						)

						final_url = canonicalize_url(page.url) or page.url
						title = (await page.title()).strip()
						html = await page.content()
						html_path.write_text(html, encoding="utf-8")

						outbound_links = await extract_links(page, final_url)
						log(f"[crawl] saved {html_path.name} title={title or '(empty)'} links={len(outbound_links)}")

					except Exception as exc:  # noqa: BLE001
						status = f"error: {exc.__class__.__name__}"
						log(f"[crawl] failed url={current_url} error={exc!r}")
						html_path.write_text(
							f"<!-- crawl failed: {current_url}\n{exc!r} -->",
							encoding="utf-8",
						)
					finally:
						await page.close()

					return CrawlRecord(
						url=current_url,
						final_url=final_url,
						title=title,
						html_path=str(html_path.relative_to(output_dir)).replace("\\", "/"),
						discovered_from=None,
						outbound_links=len(outbound_links),
						status=status,
						fetched_at=time.time(),
					)

			tasks = [fetch_target(index, url) for index, url in enumerate(selected_urls, start=1)]
			records = await asyncio.gather(*tasks)

			with manifest_path.open("w", encoding="utf-8") as manifest_file:
				for record in records:
					manifest_file.write(json.dumps(asdict(record), ensure_ascii=False) + "\n")

		finally:
			log(f"[crawl] finished. pages_saved={len(selected_urls)} manifest={manifest_path}")
			urls_path.write_text("\n".join(selected_urls), encoding="utf-8")
			await context.close()
			await browser.close()


def main() -> int:
	args = parse_args()
	targets_file = Path(args.targets_file).expanduser().resolve()
	output_dir = Path(args.output_dir).expanduser().resolve()
	output_dir.mkdir(parents=True, exist_ok=True)

	asyncio.run(
		crawl_docs(
			targets_file=targets_file,
			output_dir=output_dir,
			max_pages=args.max_pages,
			stable_ms=args.stable_ms,
			scroll_passes=args.scroll_passes,
			scroll_wait_ms=args.scroll_wait_ms,
			render_poll_ms=args.render_poll_ms,
			concurrency=args.concurrency,
			page_timeout_ms=args.page_timeout_ms,
			headful=args.headful,
			fast_mode=args.fast_mode,
		)
	)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
