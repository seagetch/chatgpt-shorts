from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from html import escape
from pathlib import Path
import re
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent
SITE_URL = "https://seagetch.github.io/chatgpt-shorts/"
DEFAULT_COLUMNS_PER_PAGE = 20
DEFAULT_ROWS_PER_COLUMN = 20
DEFAULT_BODY_FONT_MIN_PX = 12
DEFAULT_BODY_FONT_MAX_PX = 18
DATE_PREFIX_RE = re.compile(r"^(\d{8})")


@dataclass
class Block:
    kind: str
    text: str


@dataclass
class Work:
    folder: str
    title: str
    description: str
    cover: str


def main() -> None:
    generated = 0
    works: list[Work] = []
    warnings: list[str] = []

    for directory in sorted((path for path in ROOT.iterdir() if path.is_dir()), key=directory_sort_key):
        doc_path = directory / "doc.md"
        cover_png_path = directory / "title.png"
        cover_jpg_path = directory / "title.jpg"
        output_path = directory / "index.html"

        if not doc_path.is_file():
            continue

        cover_filename = ""
        if cover_png_path.is_file():
            ensure_cover_jpeg(cover_png_path, cover_jpg_path)
            cover_filename = cover_jpg_path.name
        elif cover_jpg_path.is_file():
            cover_filename = cover_jpg_path.name

        markdown = doc_path.read_text(encoding="utf-8")
        parsed_blocks = parse_markdown(markdown)
        if not parsed_blocks:
            continue

        title = next((block.text for block in parsed_blocks if block.kind == "h1"), directory.name)
        blocks = [block.__dict__ for block in parsed_blocks]
        description = build_description(blocks)
        try:
            output_path.write_text(build_html(directory.name, title, blocks, cover_filename), encoding="utf-8")
        except PermissionError as exc:
            warnings.append(f"Skipped wrapper update for {directory.name}: {exc}")
        works.append(Work(directory.name, title, description, cover_filename))
        generated += 1

    if not generated:
        raise SystemExit("No subfolders with doc.md were found.")

    (ROOT / "index.html").write_text(build_catalog_html(works), encoding="utf-8")
    print(f"Generated index.html in {generated} folders and root index.")
    for warning in warnings:
        print(warning)


def directory_sort_key(path: Path) -> tuple[int, str]:
    match = DATE_PREFIX_RE.match(path.name)
    if match:
        # Sort newer date prefixes first while keeping lexical stability inside the same date.
        return (-int(match.group(1)), path.name)
    return (10**8, path.name)


def parse_markdown(markdown_text: str) -> list[Block]:
    blocks: list[Block] = []
    paragraph_lines: list[str] = []
    pending_blank_lines = 0

    def flush_paragraph() -> None:
        nonlocal paragraph_lines, pending_blank_lines
        if not paragraph_lines:
            return

        text = "\n".join(line.strip() for line in paragraph_lines if line.strip()).strip()
        if text:
            blocks.append(Block("p", text))
            for _ in range(pending_blank_lines):
                blocks.append(Block("spacer", ""))

        paragraph_lines = []
        pending_blank_lines = 0

    normalized = markdown_text.replace("\r\n", "\n").replace("\r", "\n")
    for raw_line in normalized.split("\n"):
        stripped = raw_line.strip()

        if not stripped:
            flush_paragraph()
            pending_blank_lines += 1
            continue

        if stripped.startswith("#"):
            flush_paragraph()
            level = len(stripped) - len(stripped.lstrip("#"))
            text = stripped[level:].strip()
            if text:
                blocks.append(Block(f"h{min(level, 3)}", text))
            pending_blank_lines = 0
            continue

        paragraph_lines.append(stripped)

    flush_paragraph()
    return blocks


def ensure_cover_jpeg(source_png: Path, target_jpg: Path) -> None:
    if target_jpg.is_file() and target_jpg.stat().st_mtime >= source_png.stat().st_mtime:
        return

    source = str(source_png.resolve()).replace("\\", "\\\\")
    target = str(target_jpg.resolve()).replace("\\", "\\\\")
    powershell_script = f"""
Add-Type -AssemblyName System.Drawing
$source = "{source}"
$target = "{target}"
$image = [System.Drawing.Image]::FromFile($source)
try {{
  $encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object {{ $_.MimeType -eq 'image/jpeg' }}
  $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters 1
  $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter ([System.Drawing.Imaging.Encoder]::Quality), 95L
  $image.Save($target, $encoder, $encoderParams)
}} finally {{
  $image.Dispose()
}}
""".strip()

    subprocess.run(["powershell", "-NoProfile", "-Command", powershell_script], check=True)


def build_html(folder_name: str, title: str, blocks: list[dict[str, str]], cover_filename: str) -> str:
    description = build_description(blocks)
    page_url = build_public_url(folder_name + "/")
    cover_url = build_public_url(f"{folder_name}/{cover_filename}") if cover_filename else ""
    meta_tags = build_social_meta_tags(title, description, page_url, cover_url)
    redirect_target = f"../book.html?book={quote(folder_name)}"

    template = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>__TITLE__</title>
  __SOCIAL_META__
  <style>
    html, body {
      margin: 0;
      min-height: 100%;
      font-family: "Yu Gothic UI", "Hiragino Sans", "Meiryo", sans-serif;
      color: #2d241d;
      background: linear-gradient(180deg, #f5efe4, #e0d2bd);
    }
    body {
      display: grid;
      place-items: center;
      padding: 32px;
    }

    main {
      width: min(720px, 100%);
      padding: 32px;
      border-radius: 24px;
      border: 1px solid rgba(69, 49, 32, 0.14);
      background: rgba(255, 252, 246, 0.94);
      box-shadow: 0 24px 64px rgba(55, 36, 20, 0.18);
    }

    h1 {
      margin: 0 0 12px;
      font-size: 28px;
    }

    p {
      margin: 0;
      line-height: 1.8;
    }

    a {
      color: inherit;
    }
  </style>
</head>
<body>
  <main>
    <h1>__TITLE__</h1>
    <p>共通 reader へ移動しています。ローカル確認は HTTP 配信で行ってください。自動で進まない場合は <a id="bookLink" href="__REDIRECT_TARGET__">こちら</a> を開いてください。</p>
  </main>
  <script>
    const base = "__REDIRECT_TARGET__";
    const target = base + window.location.hash;
    document.getElementById("bookLink").href = target;
    window.location.replace(target);
  </script>
</body>
</html>
"""

    return (
        template.replace("__TITLE__", escape(title))
        .replace("__SOCIAL_META__", meta_tags)
        .replace("__REDIRECT_TARGET__", redirect_target)
    )


def build_description(blocks: list[dict[str, str]]) -> str:
    for block in blocks:
        if block["kind"] == "p" and block["text"].strip():
            text = " ".join(block["text"].split())
            return text[:110] + ("…" if len(text) > 110 else "")
    return ""


def build_public_url(path: str) -> str:
    if not SITE_URL:
        return ""

    return SITE_URL.rstrip("/") + "/" + path.lstrip("/")


def build_social_meta_tags(title: str, description: str, page_url: str, cover_url: str) -> str:
    lines = [
        '<meta property="og:type" content="article">',
        f'<meta property="og:title" content="{escape(title)}">',
        f'<meta property="og:description" content="{escape(description)}">',
        f'<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{escape(title)}">',
        f'<meta name="twitter:description" content="{escape(description)}">',
    ]

    if cover_url:
        lines.append(f'<meta property="og:image" content="{escape(cover_url)}">')
        lines.append(f'<meta property="og:image:alt" content="{escape(title)} の表紙">')
        lines.append(f'<meta name="twitter:image" content="{escape(cover_url)}">')

    if page_url:
        lines.append(f'<link rel="canonical" href="{escape(page_url)}">')
        lines.append(f'<meta property="og:url" content="{escape(page_url)}">')

    return "\n  ".join(lines)


def build_catalog_html(works: list[Work]) -> str:
    cards = []
    for work in works:
        href = f"{escape(work.folder)}/index.html"
        if work.cover:
            cover_markup = f'<img src="{escape(work.folder)}/{escape(work.cover)}" alt="{escape(work.title)} の表紙" loading="lazy">'
        else:
            cover_markup = f'<div class="card-cover-fallback"><span>{escape(work.title)}</span></div>'
        cards.append(
            f"""
      <a class="card" href="{href}">
        <div class="card-cover">
          {cover_markup}
        </div>
        <div class="card-body">
          <h2>{escape(work.title)}</h2>
          <p>{escape(work.description)}</p>
        </div>
      </a>""".rstrip()
        )

    catalog_url = build_public_url("")
    meta_lines = [
        '<meta property="og:type" content="website">',
        '<meta property="og:title" content="ChatGPT Shorts">',
        '<meta property="og:description" content="短編一覧">',
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:title" content="ChatGPT Shorts">',
        '<meta name="twitter:description" content="短編一覧">',
    ]
    if catalog_url:
        meta_lines.append(f'<link rel="canonical" href="{escape(catalog_url)}">')
        meta_lines.append(f'<meta property="og:url" content="{escape(catalog_url)}">')

    return """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>ChatGPT Shorts</title>
  __SOCIAL_META__
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@400;500;700&display=swap">
  <style>
    :root {
      color-scheme: light;
      --bg-top: #f5efe4;
      --bg-bottom: #e0d2bd;
      --paper: rgba(255, 252, 246, 0.96);
      --paper-edge: rgba(255, 248, 238, 0.94);
      --ink: #2d241d;
      --line: rgba(69, 49, 32, 0.14);
      --shadow: 0 24px 64px rgba(55, 36, 20, 0.18);
      --ui-font: "Yu Gothic UI", "Hiragino Sans", "Meiryo", sans-serif;
      --text-font: "Shippori Mincho", "Yu Mincho", "Hiragino Mincho ProN", "MS PMincho", serif;
    }

    * {
      box-sizing: border-box;
    }

    html, body {
      margin: 0;
      min-height: 100%;
      color: var(--ink);
      font-family: var(--ui-font);
      background:
        radial-gradient(circle at top, rgba(255, 255, 255, 0.46), transparent 32%),
        linear-gradient(180deg, var(--bg-top), var(--bg-bottom));
    }

    body::before {
      content: "";
      position: fixed;
      inset: 0;
      pointer-events: none;
      background-image:
        linear-gradient(rgba(255, 255, 255, 0.08) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.08) 1px, transparent 1px);
      background-size: 28px 28px;
      opacity: 0.26;
    }

    main {
      position: relative;
      z-index: 1;
      width: min(1200px, calc(100% - 40px));
      margin: 0 auto;
      padding: 48px 0 72px;
    }

    header {
      margin-bottom: 28px;
    }

    h1 {
      margin: 0;
      font-family: var(--text-font);
      font-size: clamp(32px, 4vw, 52px);
      font-weight: 500;
      letter-spacing: 0.08em;
    }

    .lead {
      margin: 14px 0 0;
      font-size: 15px;
      line-height: 1.8;
      opacity: 0.8;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 24px;
    }

    .card {
      display: grid;
      grid-template-rows: auto 1fr;
      text-decoration: none;
      color: inherit;
      background: linear-gradient(180deg, var(--paper), var(--paper-edge));
      border: 1px solid var(--line);
      border-radius: 26px;
      overflow: hidden;
      box-shadow: var(--shadow);
      transition: transform 180ms ease, box-shadow 180ms ease;
    }

    .card:hover {
      transform: translateY(-4px);
      box-shadow: 0 28px 72px rgba(55, 36, 20, 0.22);
    }

    .card-cover {
      aspect-ratio: 3 / 4;
      background: rgba(255, 255, 255, 0.42);
      border-bottom: 1px solid var(--line);
    }

    .card-cover img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .card-cover-fallback {
      display: grid;
      place-items: center;
      width: 100%;
      height: 100%;
      padding: 24px;
      background:
        radial-gradient(circle at top, rgba(255, 255, 255, 0.34), transparent 38%),
        linear-gradient(180deg, rgba(252, 247, 239, 0.94), rgba(237, 226, 209, 0.98));
      font-family: var(--text-font);
      font-size: clamp(24px, 2vw, 34px);
      line-height: 1.6;
      text-align: center;
    }

    .card-cover-fallback span {
      writing-mode: vertical-rl;
      text-orientation: mixed;
      letter-spacing: 0.12em;
    }

    .card-body {
      padding: 18px 18px 20px;
    }

    .card h2 {
      margin: 0;
      font-family: var(--text-font);
      font-size: 22px;
      font-weight: 500;
      line-height: 1.45;
    }

    .card p {
      margin: 10px 0 0;
      font-size: 14px;
      line-height: 1.8;
      opacity: 0.82;
    }
  </style>
</head>
<body>
  <main>
    <header>
      <h1>ChatGPT Shorts</h1>
      <p class="lead">各話の表紙、タイトル、導入を一覧できるトップページです。</p>
    </header>
    <section class="grid">
__CARDS__
    </section>
  </main>
</body>
</html>
""".replace("__SOCIAL_META__", "\n  ".join(meta_lines)).replace("__CARDS__", "\n".join(cards))


if __name__ == "__main__":
    main()
