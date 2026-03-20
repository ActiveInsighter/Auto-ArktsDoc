"""Convert rendered Huawei docs HTML into compact Markdown.

This converter focuses on stable extraction quality:
- keep core documentation content
- remove navigation and chrome noise
- build a reliable title and summary
- generate deterministic Markdown file names

Usage:
  python html_to_md.py --input-dir ./huawei_docs/pages --output-dir ./huawei_md

Dependencies:
  pip install beautifulsoup4 lxml
"""

from __future__ import annotations

import argparse
import html
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup, NavigableString, Tag


DEFAULT_INPUT_DIR = Path("./huawei_docs/pages")
DEFAULT_OUTPUT_DIR = Path("./huawei_md")
TOC_FILENAME = "目录.md"

REMOVABLE_TAGS = {"script", "style", "noscript", "svg"}
IGNORED_CLASS_PATTERNS = (
    "second-nav",
    "doc-header",
    "doc-header-main",
    "doc-header-box",
    "doc-header-bread",
    "anchor-list",
    "right-collapse",
    "left-side",
    "sidebar",
    "nav",
    "breadcrumb",
    "devices_box",
    "device-list",
    "device-version-list",
    "support-device-item",
    "anchor-icon",
    "handle-button",
    "handle-hover-tips",
    "expand-box",
    "expand-btn",
    "copy-button",
    "line-button",
    "theme-button",
    "ai-button",
    "document-right-menu",
    "feedback",
    "copyright",
    "footer",
    "header",
    "comment",
    "right-menu",
    "doc-right",
    "doc-left",
    "top-nav",
    "video-box",
    "screen-link-div",
    "highlight-div-header",
    "scrollbar",
)

GENERIC_TITLES = {
    "文档中心",
    "document center",
    "harmonyos开发者",
    "harmonyos developer",
}

NOISE_PARAGRAPHS = {
    "说明",
    "简介",
    "提示",
    "注意",
    "概述",
    "目录",
}

STRUCTURAL_BLOCK_TAGS = {
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "p",
    "ul",
    "ol",
    "pre",
    "table",
    "blockquote",
}


@dataclass
class Block:
    kind: str
    text: str
    markdown: str


@dataclass
class ConvertResult:
    html_path: Path
    md_path: Path
    title: str
    summary: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert Huawei docs HTML pages to Markdown.")
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--single",
        type=Path,
        default=None,
        help="Convert only one HTML file instead of scanning a directory.",
    )
    parser.add_argument(
        "--preserve-links",
        action="store_true",
        help="Keep links as Markdown links instead of plain text.",
    )
    return parser.parse_args()


def prepare_output_dir(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for markdown_file in output_dir.glob("*.md"):
        markdown_file.unlink()


def normalize_whitespace(text: str) -> str:
    text = html.unescape(text)
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[\t\r\f\v]+", " ", text)
    text = re.sub(r"[ ]{2,}", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def safe_class_text(node: Tag) -> str:
    return " ".join(node.get("class") or [])


def is_ignored_by_class(node: Tag) -> bool:
    class_text = safe_class_text(node)
    if not class_text:
        return False
    return any(pattern in class_text for pattern in IGNORED_CLASS_PATTERNS)


def clean_dom(container: Tag) -> None:
    nodes_to_remove: list[Tag] = []
    for node in container.find_all(True):
        if node.name in REMOVABLE_TAGS or node.name == "app-anchor-list":
            nodes_to_remove.append(node)
            continue
        if is_ignored_by_class(node) and node.name not in {"pre", "code", "table"}:
            nodes_to_remove.append(node)

    for node in reversed(nodes_to_remove):
        if node.parent is not None:
            node.decompose()


def score_container(candidate: Tag) -> tuple[int, int, int]:
    text = normalize_whitespace(candidate.get_text(" ", strip=True))
    if not text:
        return (0, 0, 0)

    class_names = safe_class_text(candidate)
    base_bonus = 0
    if candidate.name == "app-document-text":
        base_bonus = 5000
    elif "document-content-html" in class_names or "markdown-body" in class_names:
        base_bonus = 3500
    elif candidate.name in {"main", "article"}:
        base_bonus = 2000
    elif candidate.name == "body":
        base_bonus = 0

    semantic_count = len(
        candidate.find_all(
            ["p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "pre", "table"],
            recursive=True,
        )
    )
    return (base_bonus + len(text), semantic_count, 1 if candidate.name != "body" else 0)


def extract_main_container(soup: BeautifulSoup) -> Tag:
    candidates = [
        soup.find("app-document-text"),
        soup.find(class_="document-content-html"),
        soup.find("main"),
        soup.find("article"),
        soup.find(class_="markdown-body"),
        soup.body,
    ]

    best: Tag | None = None
    best_score = (-1, -1, -1)
    for candidate in candidates:
        if candidate is None:
            continue
        current_score = score_container(candidate)
        if current_score > best_score:
            best = candidate
            best_score = current_score

    if best is not None:
        return best
    raise ValueError("No document body found")


def render_inline(node: Tag, preserve_links: bool, base_url: str | None) -> str:
    pieces: list[str] = []
    for child in node.children:
        if isinstance(child, NavigableString):
            pieces.append(str(child))
            continue

        if child.name in {"script", "style", "noscript", "svg"}:
            continue
        if child.name in {"strong", "b"}:
            inner = render_inline(child, preserve_links, base_url)
            if inner:
                pieces.append(f"**{inner}**")
            continue
        if child.name in {"em", "i"}:
            inner = render_inline(child, preserve_links, base_url)
            if inner:
                pieces.append(f"*{inner}*")
            continue
        if child.name == "code":
            inline_code = normalize_whitespace(child.get_text(" ", strip=True))
            if inline_code:
                pieces.append(f"`{inline_code}`")
            continue
        if child.name == "br":
            pieces.append("\n")
            continue
        if child.name == "a":
            text = render_inline(child, preserve_links, base_url)
            href = (child.get("href") or "").strip()
            if not preserve_links or not href:
                pieces.append(text)
                continue
            absolute_href = urljoin(base_url, href) if base_url else href
            if text and text != absolute_href:
                pieces.append(f"[{text}]({absolute_href})")
            else:
                pieces.append(absolute_href)
            continue
        if child.name == "img":
            alt = (child.get("alt") or "").strip()
            src = (child.get("src") or "").strip()
            if src and preserve_links:
                absolute_src = urljoin(base_url, src) if base_url else src
                pieces.append(f"![{alt}]({absolute_src})" if alt else f"![]({absolute_src})")
            elif alt:
                pieces.append(alt)
            continue

        pieces.append(render_inline(child, preserve_links, base_url))

    return normalize_whitespace("".join(pieces))


def render_pre(node: Tag) -> str:
    if node.find("li") is not None:
        lines: list[str] = []
        for item in node.find_all("li", recursive=True):
            line_text = html.unescape(item.get_text("", strip=False)).replace("\r\n", "\n").replace("\r", "\n")
            line = line_text.rstrip("\n")
            if not line.strip():
                lines.append("")
            else:
                lines.append(line.rstrip())
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        return "```typescript\n" + "\n".join(lines) + "\n```" if lines else ""

    code_text = html.unescape(node.get_text("\n", strip=False)).replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in code_text.splitlines() if line.strip()]
    return "```typescript\n" + "\n".join(lines) + "\n```" if lines else ""


def render_list(node: Tag, preserve_links: bool, base_url: str | None) -> str:
    ordered = node.name == "ol"
    lines: list[str] = []
    for idx, li in enumerate(node.find_all("li", recursive=False), start=1):
        text = normalize_whitespace(render_inline(li, preserve_links, base_url))
        if not text:
            continue
        prefix = f"{idx}." if ordered else "-"
        lines.append(f"{prefix} {text}")
    return "\n".join(lines)


def render_table(table: Tag, preserve_links: bool, base_url: str | None) -> str:
    def cell_text(cell: Tag) -> str:
        return normalize_whitespace(render_inline(cell, preserve_links, base_url)).replace("\n", " ")

    header_row: list[str] | None = None
    body_rows: list[list[str]] = []

    thead = table.find("thead")
    if thead:
        row = thead.find("tr")
        if row:
            header_row = [cell_text(cell) for cell in row.find_all(["th", "td"], recursive=False)]

    tbody = table.find("tbody") or table
    for row in tbody.find_all("tr", recursive=False):
        cells = row.find_all(["th", "td"], recursive=False)
        if not cells:
            continue
        body_rows.append([cell_text(cell) for cell in cells])

    if header_row is None and body_rows:
        header_row = body_rows.pop(0)

    if not header_row:
        return ""

    width = len(header_row)
    normalized_rows: list[list[str]] = []
    for row in body_rows:
        if len(row) < width:
            row = row + [""] * (width - len(row))
        elif len(row) > width:
            row = row[:width]
        normalized_rows.append(row)

    def to_row(values: list[str]) -> str:
        return "| " + " | ".join(value.replace("\n", " ") for value in values) + " |"

    lines = [to_row(header_row), to_row(["---"] * width)]
    lines.extend(to_row(row) for row in normalized_rows)
    return "\n".join(lines)


def render_callout(node: Tag, preserve_links: bool, base_url: str | None) -> str:
    title_node = node.find(class_="title")
    content_node = node.find(class_="content")

    title = normalize_whitespace(title_node.get_text(" ", strip=True)) if title_node else "说明"
    content_source = content_node or node
    content = normalize_whitespace(content_source.get_text("\n", strip=True))
    if not content:
        return ""

    lines = [f"> **{title}**"]
    for line in content.splitlines():
        line = line.strip()
        lines.append(f"> {line}" if line else ">")
    return "\n".join(lines)


def block_kind_from_tag(node: Tag) -> str:
    if node.name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        return "heading"
    if node.name == "p":
        return "paragraph"
    if node.name in {"ul", "ol"}:
        return "list"
    if node.name == "pre":
        return "code"
    if node.name == "table":
        return "table"
    if node.name == "blockquote":
        return "quote"
    return "paragraph"


def render_structural_block(node: Tag, preserve_links: bool, base_url: str | None) -> Block | None:
    kind = block_kind_from_tag(node)

    if kind == "heading":
        level = int(node.name[1])
        text = render_inline(node, preserve_links, base_url)
        if not text:
            return None
        return Block(kind="heading", text=text, markdown=f"{'#' * level} {text}")

    if kind == "paragraph":
        text = render_inline(node, preserve_links, base_url)
        if not text:
            return None
        return Block(kind="paragraph", text=text, markdown=text)

    if kind == "list":
        markdown = render_list(node, preserve_links, base_url)
        text = normalize_whitespace(node.get_text(" ", strip=True))
        if not markdown:
            return None
        return Block(kind="list", text=text, markdown=markdown)

    if kind == "code":
        markdown = render_pre(node)
        text = normalize_whitespace(node.get_text(" ", strip=True))
        if not markdown:
            return None
        return Block(kind="code", text=text, markdown=markdown)

    if kind == "table":
        markdown = render_table(node, preserve_links, base_url)
        text = normalize_whitespace(node.get_text(" ", strip=True))
        if not markdown:
            return None
        return Block(kind="table", text=text, markdown=markdown)

    if kind == "quote":
        quote_text = normalize_whitespace(node.get_text("\n", strip=True))
        if not quote_text:
            return None
        markdown = "\n".join(f"> {line}" if line else ">" for line in quote_text.splitlines())
        return Block(kind="quote", text=quote_text, markdown=markdown)

    return None


def should_skip_subtree(node: Tag) -> bool:
    if node.name in REMOVABLE_TAGS:
        return True
    if is_ignored_by_class(node):
        return True
    return False


def collect_blocks(container: Tag, preserve_links: bool, base_url: str | None) -> list[Block]:
    blocks: list[Block] = []

    def walk(node: Tag) -> None:
        if should_skip_subtree(node):
            return

        class_names = safe_class_text(node)
        if "hw-editor-tip" in class_names:
            markdown = render_callout(node, preserve_links, base_url)
            text = normalize_whitespace(node.get_text(" ", strip=True))
            if markdown and text:
                blocks.append(Block(kind="callout", text=text, markdown=markdown))
            return

        if node.name in STRUCTURAL_BLOCK_TAGS:
            block = render_structural_block(node, preserve_links, base_url)
            if block is not None:
                blocks.append(block)
            return

        for child in node.children:
            if isinstance(child, Tag):
                walk(child)

    walk(container)

    deduped: list[Block] = []
    seen_markdown: set[str] = set()
    for block in blocks:
        key = block.markdown.strip()
        if not key or key in seen_markdown:
            continue
        seen_markdown.add(key)
        deduped.append(block)
    return deduped


def humanize_slug(slug: str) -> str:
    slug = slug.replace("_", "-").strip("- ")
    if not slug:
        return ""
    return slug.replace("-", " ")


def choose_title(
    blocks: list[Block],
    fallback_title: str,
    fallback_stem: str,
    canonical_url: str | None,
) -> str:
    for block in blocks:
        if block.kind != "heading":
            continue
        candidate = normalize_whitespace(block.text)
        if not candidate:
            continue
        if candidate.lower() in GENERIC_TITLES or candidate in GENERIC_TITLES:
            continue
        if len(candidate) <= 2:
            continue
        return candidate

    normalized_fallback = normalize_whitespace(fallback_title)
    if normalized_fallback and normalized_fallback.lower() not in GENERIC_TITLES and normalized_fallback not in GENERIC_TITLES:
        return normalized_fallback

    canonical_slug = canonical_slug_from_url(canonical_url, fallback_stem)
    if canonical_slug and not canonical_slug.isdigit() and canonical_slug.lower() not in {"index", "default", "home"}:
        readable = humanize_slug(canonical_slug)
        if readable:
            return readable

    return fallback_stem


def extract_summary_from_blocks(blocks: list[Block], max_length: int = 160) -> str:
    for block in blocks:
        if block.kind != "paragraph":
            continue
        text = normalize_whitespace(block.text)
        if not text:
            continue
        if text in NOISE_PARAGRAPHS:
            continue
        if len(text) <= 12 and not re.search(r"[。！？!?；;：,:，、]", text):
            continue
        if len(text) > max_length:
            return text[: max_length - 1].rstrip() + "…"
        return text
    return ""


def canonical_slug_from_url(canonical_url: str | None, fallback_name: str) -> str:
    if not canonical_url:
        return fallback_name

    parsed = urlparse(canonical_url)
    stem = parsed.path.rstrip("/").split("/")[-1] or fallback_name
    stem = re.sub(r"(?i)^ts(?=-)", "arkts", stem)
    stem = re.sub(r"(?i)^ts(?=_)", "arkts", stem)
    if stem.lower() == "ts":
        stem = "arkts"

    safe = re.sub(r"[^0-9A-Za-z._-]+", "-", stem).strip("-_.")
    return safe or fallback_name


def slugify_filename(text: str, fallback_name: str) -> str:
    text = normalize_whitespace(text)
    if not text:
        return fallback_name

    text = re.sub(r'[\\/:*?"<>|\x00-\x1f]+', "-", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    text = text.strip(" -._")
    if len(text) > 96:
        text = text[:96].rstrip("-._")
    return text or fallback_name


def choose_markdown_slug(canonical_url: str | None, title: str, fallback_name: str) -> str:
    url_slug = canonical_slug_from_url(canonical_url, fallback_name)
    lower_slug = url_slug.lower()
    bad_slug = (
        url_slug.isdigit()
        or lower_slug in {"index", "default", "home", fallback_name.lower()}
        or lower_slug.startswith("document")
    )

    if bad_slug:
        title_slug = slugify_filename(title, fallback_name)
        if title_slug and title_slug != fallback_name:
            return title_slug
    return url_slug


def build_markdown(title: str, base_url: str | None, blocks: list[Block]) -> str:
    lines: list[str] = [f"# {title}"]
    if base_url:
        lines.append(f"来源: {base_url}")
    lines.append("")

    start_index = 0
    if blocks and blocks[0].kind == "heading" and normalize_whitespace(blocks[0].text) == normalize_whitespace(title):
        start_index = 1

    for block in blocks[start_index:]:
        markdown = block.markdown.strip()
        if not markdown:
            continue
        lines.append(markdown)
        lines.append("")

    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip() + "\n"


def build_toc_markdown(results: list[ConvertResult]) -> str:
    def clean_cell(text: str) -> str:
        text = re.sub(r"\s+", " ", text).strip()
        return text.replace("|", "\\|")

    lines = ["# 目录", "", "| 编号 | 标题 | 简介 |", "| --- | --- | --- |"]
    for index, result in enumerate(results, start=1):
        relative_name = result.md_path.name
        title = clean_cell(result.title)
        summary = clean_cell(result.summary)
        lines.append(f"| {index:03d} | [打开]({relative_name}) | {title} | {summary} |")
    return "\n".join(lines).strip() + "\n"


def write_markdown(
    html_path: Path,
    output_dir: Path,
    serial: int,
    preserve_links: bool,
) -> ConvertResult:
    raw_html = html_path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(raw_html, "lxml")

    fallback_title = normalize_whitespace(soup.title.get_text(" ", strip=True)) if soup.title else html_path.stem
    canonical = soup.select_one('link[rel="canonical"]')
    base_url = canonical.get("href") if canonical else None

    container = extract_main_container(soup)
    clean_dom(container)
    blocks = collect_blocks(container, preserve_links=preserve_links, base_url=base_url)

    title = choose_title(
        blocks,
        fallback_title=fallback_title,
        fallback_stem=html_path.stem,
        canonical_url=base_url,
    )
    summary = extract_summary_from_blocks(blocks)

    markdown_text = build_markdown(title=title, base_url=base_url, blocks=blocks)
    slug = choose_markdown_slug(base_url, title, html_path.stem)

    md_path = output_dir / f"{serial:03d}_{slug}.md"
    md_path.write_text(markdown_text, encoding="utf-8")

    return ConvertResult(html_path=html_path, md_path=md_path, title=title, summary=summary)


def iter_html_files(input_dir: Path, single: Path | None) -> Iterable[Path]:
    if single is not None:
        yield single
        return
    yield from sorted(input_dir.glob("*.html"))


def main() -> int:
    args = parse_args()
    input_dir = args.input_dir.expanduser().resolve()
    output_dir = args.output_dir.expanduser().resolve()

    prepare_output_dir(output_dir)

    html_files = list(iter_html_files(input_dir, args.single))
    if not html_files:
        raise FileNotFoundError(f"No HTML files found in {input_dir}")

    results: list[ConvertResult] = []
    for serial, html_path in enumerate(html_files, start=1):
        result = write_markdown(
            html_path=html_path,
            output_dir=output_dir,
            serial=serial,
            preserve_links=args.preserve_links,
        )
        results.append(result)
        print(f"[ok] {html_path.name} -> {result.md_path.name}")

    toc_path = output_dir / TOC_FILENAME
    toc_path.write_text(build_toc_markdown(results), encoding="utf-8")
    print(f"Converted {len(results)} file(s) into {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
