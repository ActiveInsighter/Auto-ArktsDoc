"""Convert rendered Huawei docs HTML into compact Markdown.

The converter keeps the useful documentation content and strips the noisy UI
chrome such as navigation, breadcrumbs, sidebars, device labels, and toolbars.
It focuses on:
- headings
- paragraphs
- lists
- tables
- code blocks
- note/info callouts

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
    "second-nav",
    "video-box",
    "screen-link-div",
    "highlight-div-header",
    "scrollbar",
)

BLOCK_TAGS = {
    "article",
    "aside",
    "blockquote",
    "div",
    "dl",
    "dt",
    "dd",
    "figure",
    "figcaption",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hr",
    "li",
    "ol",
    "p",
    "pre",
    "section",
    "table",
    "tbody",
    "td",
    "tfoot",
    "th",
    "thead",
    "tr",
    "ul",
}


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


def is_ignored_node(node: Tag) -> bool:
    classes = node.get("class") or []
    return any(
        ignored in " ".join(classes)
        for ignored in IGNORED_CLASS_PATTERNS
    )


def canonical_slug_from_url(canonical_url: str | None, fallback_name: str) -> str:
    if canonical_url:
        parsed = urlparse(canonical_url)
        stem = parsed.path.rstrip("/").split("/")[-1] or fallback_name
    else:
        stem = fallback_name

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
    if len(text) > 80:
        text = text[:80].rstrip("-._")
    return text or fallback_name


def choose_markdown_slug(canonical_url: str | None, title: str, fallback_name: str) -> str:
    url_slug = canonical_slug_from_url(canonical_url, fallback_name)
    if url_slug.isdigit() or url_slug.lower() in {fallback_name.lower(), "index", "default", "home"}:
        title_slug = slugify_filename(title, fallback_name)
        if title_slug and title_slug != fallback_name:
            return title_slug
    return url_slug


def has_block_children(node: Tag) -> bool:
    for child in node.children:
        if not isinstance(child, Tag):
            continue
        if child.name in BLOCK_TAGS:
            return True
    return False


def render_node(node: Tag | NavigableString, preserve_links: bool, base_url: str | None) -> str:
    if isinstance(node, NavigableString):
        return str(node)

    if not isinstance(node, Tag):
        return ""

    if node.name in {"script", "style", "noscript", "svg"}:
        return ""

    if node.name == "br":
        return "\n"

    if node.name in {"strong", "b"}:
        inner = render_inline_children(node, preserve_links, base_url)
        return f"**{inner}**" if inner else ""

    if node.name in {"em", "i"}:
        inner = render_inline_children(node, preserve_links, base_url)
        return f"*{inner}*" if inner else ""

    if node.name == "code":
        return f"`{normalize_whitespace(node.get_text(' ', strip=True))}`"

    if node.name == "a":
        text = render_inline_children(node, preserve_links, base_url)
        href = node.get("href", "").strip()
        if not preserve_links or not href:
            return text
        absolute_href = urljoin(base_url, href) if base_url else href
        if text and text != absolute_href:
            return f"[{text}]({absolute_href})"
        return absolute_href

    if node.name == "img":
        alt = node.get("alt", "")
        src = node.get("src", "")
        if src and preserve_links:
            absolute_src = urljoin(base_url, src) if base_url else src
            return f"![{alt}]({absolute_src})" if alt else f"![]({absolute_src})"
        return alt

    if node.name == "pre":
        return render_pre(node)

    if node.name == "table":
        return render_table(node, preserve_links, base_url)

    if node.name in {"ul", "ol"}:
        return render_list(node, preserve_links, base_url)

    if node.name == "li":
        return render_list_item(node, preserve_links, base_url)

    if node.name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        level = int(node.name[1])
        text = render_inline_children(node, preserve_links, base_url)
        return f"{'#' * level} {text}".strip() if text else ""

    if node.name == "blockquote":
        inner = render_block(node, preserve_links, base_url)
        if not inner:
            return ""
        lines = [f"> {line}" if line.strip() else ">" for line in inner.splitlines()]
        return "\n".join(lines)

    if node.name == "hr":
        return "---"

    if node.name in {"div", "section", "article", "main", "aside"}:
        class_names = " ".join(node.get("class") or [])
        if "hw-editor-tip" in class_names:
            return render_callout(node, preserve_links, base_url)
        if "highlight-scroll-div" in class_names:
            pre = node.find("pre")
            return render_pre(pre) if pre else ""
        if "tablenoborder" in class_names or "tbBox" in class_names or "tiledSection" in class_names:
            return render_block(node, preserve_links, base_url)
        if has_block_children(node):
            return render_block(node, preserve_links, base_url)
        return render_inline_children(node, preserve_links, base_url)

    return render_inline_children(node, preserve_links, base_url)


def render_inline_children(node: Tag, preserve_links: bool, base_url: str | None) -> str:
    pieces: list[str] = []
    for child in node.children:
        if isinstance(child, NavigableString):
            pieces.append(str(child))
        else:
            pieces.append(render_node(child, preserve_links, base_url))
    return normalize_whitespace("".join(pieces))


def render_list_item(node: Tag, preserve_links: bool, base_url: str | None) -> str:
    parts: list[str] = []
    for child in node.children:
        if isinstance(child, NavigableString):
            parts.append(str(child))
        else:
            parts.append(render_node(child, preserve_links, base_url))
    text = normalize_whitespace("".join(parts))
    text = re.sub(r"\n+", " ", text)
    return text


def render_pre(node: Tag) -> str:
    if node is None:
        return ""

    if node.find("li") is not None:
        list_items = node.find_all("li", recursive=True)
        lines: list[str] = []
        for item in list_items:
            line_html = item.get_text("", strip=False)
            line_html = html.unescape(line_html)
            line_html = line_html.replace("\r\n", "\n").replace("\r", "\n")
            line = line_html.rstrip("\n")
            if not line.strip():
                lines.append("")
                continue
            lines.append(line.rstrip())
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        return "```typescript\n" + "\n".join(lines) + "\n```" if lines else ""

    code = node.get_text("\n", strip=False)
    code = html.unescape(code)
    code = code.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in code.splitlines()]
    lines = [line for line in lines if line.strip()]
    return "```typescript\n" + "\n".join(lines) + "\n```" if lines else ""


def cell_text(cell: Tag, preserve_links: bool, base_url: str | None) -> str:
    pieces: list[str] = []
    for child in cell.children:
        if isinstance(child, NavigableString):
            pieces.append(str(child))
        else:
            pieces.append(render_node(child, preserve_links, base_url))
    text = normalize_whitespace("".join(pieces))
    text = re.sub(r"\n+", " ", text)
    return text


def render_table(table: Tag, preserve_links: bool, base_url: str | None) -> str:
    header_row: list[str] | None = None
    body_rows: list[list[str]] = []

    thead = table.find("thead")
    if thead:
        row = thead.find("tr")
        if row:
            header_row = [cell_text(th, preserve_links, base_url) for th in row.find_all(["th", "td"], recursive=False)]

    tbody = table.find("tbody") or table
    for row in tbody.find_all("tr", recursive=False):
        cells = row.find_all(["th", "td"], recursive=False)
        if not cells:
            continue
        body_rows.append([cell_text(cell, preserve_links, base_url) for cell in cells])

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
    content = ""
    if content_node:
        content = render_block(content_node, preserve_links, base_url)
    else:
        content = render_block(node, preserve_links, base_url)
    content = content.strip()
    if not content:
        return ""
    lines = [f"> **{title}**"]
    for line in content.splitlines():
        lines.append(f"> {line}" if line.strip() else ">")
    return "\n".join(lines)


def render_block(node: Tag, preserve_links: bool, base_url: str | None) -> str:
    chunks: list[str] = []
    for child in node.children:
        rendered = render_node(child, preserve_links, base_url)
        rendered = rendered.strip()
        if rendered:
            chunks.append(rendered)
    return collapse_blocks(chunks)


def collapse_blocks(chunks: Iterable[str]) -> str:
    out: list[str] = []
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue
        if out and out[-1] != "":
            out.append("")
        out.extend(chunk.splitlines())
    return "\n".join(out).strip()


def extract_main_container(soup: BeautifulSoup) -> Tag:
    candidates = [
        soup.find("app-document-text"),
        soup.find(class_="document-content-html"),
        soup.find("main"),
        soup.find("article"),
        soup.find(class_="markdown-body"),
        soup.body,
    ]
    best_candidate: Tag | None = None
    best_score = (-1, -1, -1)
    for candidate in candidates:
        if candidate is None:
            continue

        text = normalize_whitespace(candidate.get_text(" ", strip=True))
        if not text:
            score = (0, 0, 0)
        else:
            class_names = " ".join(candidate.get("class") or [])
            bonus = 0
            if candidate.name == "app-document-text":
                bonus = 3000
            elif "document-content-html" in class_names or "markdown-body" in class_names:
                bonus = 2000
            elif candidate.name in {"main", "article"}:
                bonus = 1000
            node_count = len(candidate.find_all(["p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "pre", "table"], recursive=True))
            score = (bonus + len(text), node_count, 1 if candidate.name != "body" else 0)

        if score > best_score:
            best_candidate = candidate
            best_score = score

    if best_candidate is not None:
        return best_candidate
    for candidate in candidates:
        if candidate is not None:
            return candidate
    raise ValueError("No document body found")


def clean_dom(container: Tag) -> None:
    nodes_to_remove: list[Tag] = []
    for node in container.find_all(True):
        if not isinstance(node, Tag):
            continue
        if node.name in REMOVABLE_TAGS or node.name == "app-anchor-list":
            nodes_to_remove.append(node)
            continue
        class_values = node.attrs.get("class") if getattr(node, "attrs", None) else None
        if not class_values:
            continue
        classes = " ".join(class_values)
        if any(part in classes for part in IGNORED_CLASS_PATTERNS):
            if node.name not in {"pre", "code", "table"}:
                nodes_to_remove.append(node)

    for node in reversed(nodes_to_remove):
        if getattr(node, "parent", None) is not None:
            node.decompose()


def gather_blocks(container: Tag, preserve_links: bool, base_url: str | None) -> list[str]:
    blocks: list[str] = []
    for child in container.children:
        rendered = render_node(child, preserve_links, base_url)
        if rendered:
            blocks.append(rendered)
    return blocks


def render_list(node: Tag, preserve_links: bool, base_url: str | None) -> str:
    ordered = node.name == "ol"
    items: list[str] = []
    for index, li in enumerate(node.find_all("li", recursive=False), start=1):
        text = render_list_item(li, preserve_links, base_url)
        if not text:
            continue
        prefix = f"{index}." if ordered else "-"
        items.append(f"{prefix} {text}")
    return "\n".join(items)


def render_blockquote(node: Tag, preserve_links: bool, base_url: str | None) -> str:
    rendered = render_block(node, preserve_links, base_url)
    if not rendered:
        return ""
    return "\n".join((f"> {line}" if line else ">") for line in rendered.splitlines())


def extract_summary_from_markdown(markdown_text: str, max_length: int = 160) -> str:
    lines = markdown_text.splitlines()
    index = 0

    if index < len(lines) and lines[index].startswith("# "):
        index += 1

    while index < len(lines) and not lines[index].strip():
        index += 1

    if index < len(lines) and lines[index].startswith("来源:"):
        index += 1

    while index < len(lines) and not lines[index].strip():
        index += 1

    paragraph_lines: list[str] = []
    while index < len(lines):
        line = lines[index].strip()
        if not line:
            break
        if not paragraph_lines and line.startswith(("#", ">", "|", "```")):
            index += 1
            continue
        if paragraph_lines and line.startswith(("#", ">", "|", "```")):
            break
        paragraph_lines.append(line)
        index += 1

    summary = re.sub(r"\s+", " ", " ".join(paragraph_lines)).strip()
    if len(summary) > max_length:
        summary = summary[: max_length - 1].rstrip() + "…"
    return summary


def extract_summary_from_blocks(blocks: Iterable[str], max_length: int = 160) -> str:
    for block in blocks:
        candidate = re.sub(r"\s+", " ", block).strip()
        if not candidate:
            continue
        if candidate.startswith(("#", ">", "|", "```", "- ", "* ")):
            continue
        if candidate in {"说明", "简介", "提示", "注意", "概述", "目录"}:
            continue
        if len(candidate) <= 12 and not re.search(r"[。！？!?；;：,:，、]", candidate):
            continue
        if len(candidate) > max_length:
            candidate = candidate[: max_length - 1].rstrip() + "…"
        return candidate
    return ""


def build_toc_markdown(results: list[ConvertResult]) -> str:
    def clean_cell(text: str) -> str:
        text = re.sub(r"\s+", " ", text).strip()
        return text.replace("|", "\\|")

    lines = ["# 目录", "", "| 编号 | 标题 | 简介 |", "| --- | --- | --- |"]
    for result in results:
        relative_name = result.md_path.name
        title = clean_cell(result.title)
        description = clean_cell(result.summary or "")
        lines.append(
            f"| {relative_name[:3]} | [打开]({relative_name}) | {title} | {description} |"
        )
    return "\n".join(lines).strip() + "\n"


def write_markdown(html_path: Path, output_dir: Path, preserve_links: bool) -> ConvertResult:
    raw_html = html_path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(raw_html, "lxml")
    title = normalize_whitespace(soup.title.get_text(" ", strip=True)) if soup.title else html_path.stem
    canonical = soup.select_one('link[rel="canonical"]')
    base_url = canonical.get("href") if canonical else None
    container = extract_main_container(soup)
    clean_dom(container)

    blocks = gather_blocks(container, preserve_links=preserve_links, base_url=base_url)
    md_parts: list[str] = []
    md_parts.append(f"# {title}")
    if base_url:
        md_parts.append(f"来源: {base_url}")
    md_parts.append("")
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        md_parts.append(block)
        md_parts.append("")

    markdown_text = re.sub(r"\n{3,}", "\n\n", "\n".join(md_parts)).strip() + "\n"
    summary = extract_summary_from_blocks(blocks) or extract_summary_from_markdown(markdown_text)
    md_name = choose_markdown_slug(base_url, title, html_path.stem)
    md_path = output_dir / f"{len(list(output_dir.glob('*.md'))) + 1:03d}_{md_name}.md"
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
    for html_path in html_files:
        result = write_markdown(html_path, output_dir, preserve_links=args.preserve_links)
        results.append(result)
        print(f"[ok] {html_path.name} -> {result.md_path.name}")

    toc_path = output_dir / TOC_FILENAME
    toc_path.write_text(build_toc_markdown(results), encoding="utf-8")
    print(f"Converted {len(results)} file(s) into {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
