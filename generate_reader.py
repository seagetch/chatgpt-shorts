from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SITE_URL = "https://seagetch.github.io/chatgpt-shorts/"
DEFAULT_COLUMNS_PER_PAGE = 20
DEFAULT_ROWS_PER_COLUMN = 20
DEFAULT_BODY_FONT_MIN_PX = 12
DEFAULT_BODY_FONT_MAX_PX = 18


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

    for directory in sorted(path for path in ROOT.iterdir() if path.is_dir()):
        doc_path = directory / "doc.md"
        cover_png_path = directory / "title.png"
        cover_jpg_path = directory / "title.jpg"
        output_path = directory / "index.html"

        if not doc_path.is_file() or not cover_png_path.is_file():
            continue

        ensure_cover_jpeg(cover_png_path, cover_jpg_path)

        markdown = doc_path.read_text(encoding="utf-8")
        blocks = [block.__dict__ for block in parse_markdown(markdown)]
        if not blocks:
            continue

        title = next((block["text"] for block in blocks if block["kind"] == "h1"), directory.name)
        description = build_description(blocks)
        output_path.write_text(build_html(directory.name, title, blocks, cover_jpg_path.name), encoding="utf-8")
        works.append(Work(directory.name, title, description, cover_jpg_path.name))
        generated += 1

    if not generated:
        raise SystemExit("No subfolders with both doc.md and title.png were found.")

    (ROOT / "index.html").write_text(build_catalog_html(works), encoding="utf-8")
    print(f"Generated index.html in {generated} folders and root index.")


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
    blocks_json = json.dumps(blocks, ensure_ascii=False)
    description = build_description(blocks)
    page_url = build_public_url(folder_name + "/")
    cover_url = build_public_url(f"{folder_name}/{cover_filename}")
    meta_tags = build_social_meta_tags(title, description, page_url, cover_url)
    reader_config_json = json.dumps(
        {
            "columnsPerPage": DEFAULT_COLUMNS_PER_PAGE,
            "rowsPerColumn": DEFAULT_ROWS_PER_COLUMN,
            "bodyFontMinPx": DEFAULT_BODY_FONT_MIN_PX,
            "bodyFontMaxPx": DEFAULT_BODY_FONT_MAX_PX,
        },
        ensure_ascii=False,
    )

    template = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>__TITLE__</title>
  __SOCIAL_META__
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link
    id="readerFontStylesheet"
    rel="stylesheet"
    href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@400;500;700&display=swap"
  >
  <style>
    :root {
      color-scheme: light;
      --bg-top: #f5efe4;
      --bg-bottom: #e0d2bd;
      --paper: rgba(255, 252, 246, 0.98);
      --paper-edge: rgba(255, 248, 238, 0.94);
      --ink: #2d241d;
      --line: rgba(69, 49, 32, 0.14);
      --shadow: 0 24px 64px rgba(55, 36, 20, 0.18);
      --sheet-width-single: 780px;
      --sheet-width-double: 540px;
      --sheet-height: 1040px;
      --sheet-pad-top: 34px;
      --sheet-pad-right: 34px;
      --sheet-pad-bottom: 34px;
      --sheet-pad-left: 34px;
      --content-height: 720px;
      --content-width: 560px;
      --lines-per-page: 20;
      --spread-gap: clamp(14px, 1.8vw, 24px);
      --body-font-size: __BODY_FONT_MAX__px;
      --body-line-height: 1.24;
      --line-pitch: 24px;
      --body-letter-spacing: 0.03em;
      --ui-font: "Yu Gothic UI", "Hiragino Sans", "Meiryo", sans-serif;
      --text-font: "Shippori Mincho", "Yu Mincho", "Hiragino Mincho ProN", "MS PMincho", serif;
    }

    * {
      box-sizing: border-box;
    }

    html, body {
      height: 100%;
      margin: 0;
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

    .app {
      min-height: 100%;
      display: grid;
      grid-template-rows: 1fr auto;
      gap: 18px;
      padding: 24px;
      position: relative;
    }

    .reader-frame {
      display: flex;
      justify-content: center;
      align-items: flex-start;
      width: 100%;
      min-height: 0;
      overflow-x: auto;
      overflow-y: hidden;
      scroll-behavior: auto;
    }

    .spread {
      display: flex;
      flex-direction: row-reverse;
      align-items: stretch;
      justify-content: center;
      gap: var(--spread-gap);
      width: max-content;
      min-height: 0;
      flex: 0 0 auto;
      margin-inline: auto;
    }

    .spread[data-mode="single"] {
      max-width: var(--sheet-width-single);
    }

    .spread[data-mode="double"] {
      max-width: calc(var(--sheet-width-double) * 2 + var(--spread-gap));
    }

    .sheet {
      position: relative;
      width: var(--sheet-width-single);
      height: var(--sheet-height);
      border-radius: 28px;
      border: 1px solid rgba(65, 45, 28, 0.12);
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.54), transparent 18%),
        linear-gradient(135deg, var(--paper), var(--paper-edge));
      box-shadow: var(--shadow);
      overflow: hidden;
      flex: 0 0 auto;
    }

    .spread[data-mode="double"] .sheet {
      width: var(--sheet-width-double);
    }

    .sheet::before {
      content: "";
      position: absolute;
      inset: 0;
      pointer-events: none;
      background:
        linear-gradient(90deg, transparent, rgba(120, 86, 58, 0.05) 50%, transparent),
        radial-gradient(circle at center, transparent 62%, rgba(109, 73, 45, 0.04) 100%);
    }

    .sheet--left::after,
    .sheet--right::after {
      content: "";
      position: absolute;
      top: 5%;
      bottom: 5%;
      width: 18px;
      pointer-events: none;
      opacity: 0.22;
      filter: blur(8px);
    }

    .sheet--left::after {
      left: -9px;
      background: linear-gradient(90deg, rgba(74, 51, 31, 0.22), transparent);
    }

    .sheet--right::after {
      right: -9px;
      background: linear-gradient(270deg, rgba(74, 51, 31, 0.22), transparent);
    }

    .sheet--blank {
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.38), transparent 18%),
        linear-gradient(135deg, rgba(255, 250, 243, 0.8), rgba(247, 239, 227, 0.9));
    }

    .sheet-cover {
      display: grid;
      grid-template-rows: 1fr auto;
      height: 100%;
      padding: 22px;
      gap: 14px;
    }

    .sheet-cover img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      border-radius: 20px;
      background: rgba(244, 236, 225, 0.78);
      box-shadow: inset 0 0 0 1px rgba(84, 57, 34, 0.08);
    }

    .cover-meta {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      font-size: 13px;
      opacity: 0.72;
    }

    .sheet-text {
      position: relative;
      width: 100%;
      height: 100%;
      overflow: hidden;
      padding: 0;
    }

    .sheet-text h1,
    .sheet-text h2,
    .sheet-text h3,
    .sheet-text p {
      margin: 0;
    }

    .sheet-text .spacer {
      inline-size: 100%;
      block-size: var(--line-pitch);
    }

    .sheet-text h1,
    .sheet-text h2,
    .sheet-text h3 {
      font-weight: 600;
      letter-spacing: 0.12em;
    }

    .sheet-text h1 {
      font-size: 1.3em;
    }

    .sheet-text h2 {
      font-size: 1.12em;
    }

    .sheet-text h3 {
      font-size: 1.02em;
    }

    .sheet-text p {
      white-space: pre-wrap;
    }

    .sheet-text-inner {
      position: absolute;
      top: var(--sheet-pad-top);
      right: var(--sheet-pad-right);
      inline-size: var(--content-height);
      block-size: var(--content-width);
      writing-mode: vertical-rl;
      text-orientation: mixed;
      overflow: hidden;
      font-family: var(--text-font);
      font-size: var(--body-font-size);
      line-height: var(--body-line-height);
      letter-spacing: var(--body-letter-spacing);
      word-break: normal;
      overflow-wrap: anywhere;
      line-break: strict;
      hanging-punctuation: allow-end;
      font-kerning: normal;
      -webkit-text-size-adjust: 100%;
    }

    .sheet-text-inner > * + * {
      margin-block-start: 0;
    }

    .measure-sheet {
      position: fixed;
      left: -9999px;
      top: 0;
      visibility: hidden;
      overflow: visible;
      pointer-events: none;
      z-index: -1;
    }

    .measure-sheet .sheet-text {
      position: absolute;
      top: var(--sheet-pad-top);
      right: var(--sheet-pad-right);
      width: var(--content-width);
      height: var(--content-height);
      overflow: hidden;
      padding: 0;
    }

    .measure-sheet .sheet-text-inner {
      position: static;
      inset: auto;
      display: block;
      inline-size: auto;
      block-size: auto;
      min-inline-size: var(--content-height);
      min-block-size: var(--content-width);
      min-height: 0;
      overflow: visible;
    }

    .footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
      padding: 16px 20px;
      border: 1px solid var(--line);
      border-radius: 20px;
      background: rgba(252, 247, 239, 0.78);
      backdrop-filter: blur(12px);
      box-shadow: var(--shadow);
    }

    .controls {
      display: flex;
      gap: 10px;
      align-items: center;
      flex-wrap: wrap;
    }

    button {
      appearance: none;
      border: 1px solid rgba(70, 48, 30, 0.18);
      border-radius: 999px;
      background: var(--paper);
      color: var(--ink);
      font: inherit;
      padding: 10px 16px;
      cursor: pointer;
      transition: transform 160ms ease, background 160ms ease, opacity 160ms ease;
    }

    button:hover {
      transform: translateY(-1px);
      background: #fffdf9;
    }

    button:disabled {
      cursor: default;
      opacity: 0.42;
      transform: none;
    }

    .page-indicator {
      min-width: 110px;
      text-align: center;
      font-size: 14px;
      opacity: 0.82;
    }

    .hint {
      margin: 0;
      font-size: 13px;
      opacity: 0.72;
    }

    @media (max-width: 1100px) {
      .app {
        padding: 16px;
      }

      :root {
        --sheet-width-single: 720px;
        --sheet-width-double: 350px;
        --sheet-height: 960px;
        --sheet-pad-top: 26px;
        --sheet-pad-right: 26px;
        --sheet-pad-bottom: 26px;
        --sheet-pad-left: 26px;
      }
    }

    @media (max-width: 640px) {
      .footer {
        justify-content: center;
        text-align: center;
      }

      .controls {
        justify-content: center;
      }

      .cover-meta {
        flex-direction: column;
        align-items: flex-start;
      }
    }
  </style>
</head>
<body>
  <div class="app">
    <main class="reader-frame">
      <div id="spreadHost" class="spread" data-mode="single"></div>
    </main>

    <footer class="footer">
      <div class="controls">
        <button id="nextButton" type="button">次の頁</button>
        <button id="prevButton" type="button">前の頁</button>
      </div>
      <div id="pageIndicator" class="page-indicator"></div>
      <p class="hint">操作: ← 次の頁 / → 前の頁 / Swipe / Home 表紙 / End 最終頁</p>
    </footer>
  </div>

  <script>
    const READER_CONFIG = __READER_CONFIG__;
    const work = {
      folder: "__FOLDER__",
      title: "__TITLE__",
      cover: "__COVER__",
      blocks: __BLOCKS_JSON__,
    };

    const state = {
      pages: [],
      currentPageIndex: 0,
      spreadMode: false,
    };

    const readerFrame = document.querySelector(".reader-frame");
    const spreadHost = document.getElementById("spreadHost");
    const pageIndicator = document.getElementById("pageIndicator");
    const prevButton = document.getElementById("prevButton");
    const nextButton = document.getElementById("nextButton");

    initialize();

    async function initialize() {
      bindEvents();
      await waitForFonts();
      refreshLayout(true);
      goToPage(parseHashPage(), false);
    }

    async function waitForFonts() {
      const timeout = new Promise((resolve) => window.setTimeout(resolve, 8000));
      const pending = [];
      const fontStylesheet = document.getElementById("readerFontStylesheet");

      if (fontStylesheet && !fontStylesheet.sheet) {
        pending.push(new Promise((resolve) => {
          const finish = () => {
            fontStylesheet.removeEventListener("load", finish);
            fontStylesheet.removeEventListener("error", finish);
            resolve();
          };

          fontStylesheet.addEventListener("load", finish, { once: true });
          fontStylesheet.addEventListener("error", finish, { once: true });
        }));
      }

      if (document.fonts) {
        pending.push(
          Promise.all([
            document.fonts.ready.catch(() => undefined),
            document.fonts.load('400 16px "Shippori Mincho"').catch(() => undefined),
            document.fonts.load('500 16px "Shippori Mincho"').catch(() => undefined),
            document.fonts.load('700 16px "Shippori Mincho"').catch(() => undefined),
          ]),
        );
      }

      if (pending.length === 0) {
        return;
      }

      await Promise.race([
        Promise.all(pending),
        timeout,
      ]);
    }

    function bindEvents() {
      nextButton.addEventListener("click", () => goToPage(getNextIndex()));
      prevButton.addEventListener("click", () => goToPage(getPrevIndex()));

      document.addEventListener("keydown", (event) => {
        if (event.key === "ArrowLeft") {
          event.preventDefault();
          goToPage(getNextIndex());
        } else if (event.key === "ArrowRight") {
          event.preventDefault();
          goToPage(getPrevIndex());
        } else if (event.key === "Home") {
          event.preventDefault();
          goToPage(0);
        } else if (event.key === "End") {
          event.preventDefault();
          goToPage(state.spreadMode ? getLastSpreadStartIndex() : state.pages.length - 1);
        }
      });

      let touchStartX = 0;
      let touchStartY = 0;

      spreadHost.addEventListener("touchstart", (event) => {
        const touch = event.changedTouches[0];
        touchStartX = touch.clientX;
        touchStartY = touch.clientY;
      }, { passive: true });

      spreadHost.addEventListener("touchend", (event) => {
        const touch = event.changedTouches[0];
        const dx = touch.clientX - touchStartX;
        const dy = touch.clientY - touchStartY;

        if (Math.abs(dx) < 40 || Math.abs(dx) < Math.abs(dy)) {
          return;
        }

        if (dx < 0) {
          goToPage(getNextIndex());
        } else {
          goToPage(getPrevIndex());
        }
      }, { passive: true });

      window.addEventListener("resize", () => {
        const currentIndex = state.currentPageIndex;
        refreshLayout(true);
        goToPage(currentIndex, false);
      });

      window.addEventListener("hashchange", () => {
        goToPage(parseHashPage(), false);
      });
    }

    function refreshLayout(forceRepaginate) {
      const nextSpreadMode = shouldUseSpreadMode();
      const modeChanged = nextSpreadMode !== state.spreadMode;

      state.spreadMode = nextSpreadMode;
      spreadHost.dataset.mode = state.spreadMode ? "double" : "single";
      applyLayoutMetrics();

      if (forceRepaginate || modeChanged || state.pages.length === 0) {
        state.pages = paginateWork(work);
      }
    }

    function shouldUseSpreadMode() {
      return window.innerWidth >= 1100 && window.innerWidth > window.innerHeight * 1.12;
    }

    function applyLayoutMetrics() {
      const root = document.documentElement;
      const compact = window.innerWidth <= 1100;
      const maxFontWidthFillRatio = 0.8;
      const outerPadding = compact ? 32 : 48;
      const verticalPadding = compact ? 32 : 48;
      const spreadGap = compact ? 16 : 24;
      const footerReserve = compact ? 92 : 104;
      const sheetHeight = Math.max(360, window.innerHeight - footerReserve - verticalPadding);
      const aspectWidth = Math.floor(sheetHeight * 3 / 4);
      const maxSingleWidth = Math.max(320, window.innerWidth - outerPadding);
      const maxDoubleWidth = Math.max(220, Math.floor((window.innerWidth - outerPadding - spreadGap) / 2));
      const sheetWidthSingle = Math.min(aspectWidth, maxSingleWidth);
      const sheetWidthDouble = Math.min(aspectWidth, maxDoubleWidth);
      const activeSheetWidth = state.spreadMode ? sheetWidthDouble : sheetWidthSingle;

      const targetLinesPerPage = Math.max(1, READER_CONFIG.columnsPerPage);
      const targetCharsPerLine = Math.max(1, READER_CONFIG.rowsPerColumn);
      const minFont = Number(READER_CONFIG.bodyFontMinPx) || 12;
      const maxFont = Number(READER_CONFIG.bodyFontMaxPx) || 18;
      const lineHeight = compact ? 1.22 : 1.24;
      const letterSpacingEm = 0.03;
      const baseTopPadding = (compact ? 26 : 34) + (compact ? 8 : 10);
      const baseBottomPadding = compact ? 26 : 34;
      const baseSidePadding = compact ? 28 : 40;
      const maxContentHeight = Math.max(240, sheetHeight - baseTopPadding - baseBottomPadding);
      const maxContentWidth = Math.max(160, activeSheetWidth - baseSidePadding * 2);

      const fontSizeFromWidth = maxContentWidth / (targetLinesPerPage * lineHeight);
      const fontSizeFromHeight = maxContentHeight / (targetCharsPerLine * (1 + letterSpacingEm));
      const fontSize = clamp(Math.min(fontSizeFromWidth, fontSizeFromHeight), minFont, maxFont);
      const linePitch = fontSize * lineHeight;
      const contentHeight = Math.round(maxContentHeight);
      const naturalContentWidth = Math.round(linePitch * targetLinesPerPage);
      const minFilledContentWidth = Math.round(maxContentWidth * maxFontWidthFillRatio);
      const isAtMaxFont = fontSize >= maxFont - 0.01;
      const contentWidth = Math.min(
        maxContentWidth,
        isAtMaxFont ? Math.max(naturalContentWidth, minFilledContentWidth) : naturalContentWidth,
      );

      const topPadding = baseTopPadding;
      const bottomPadding = baseBottomPadding;
      const extraHorizontal = Math.max(0, activeSheetWidth - contentWidth);
      const sidePadding = Math.max(baseSidePadding, Math.floor(extraHorizontal / 2));

      root.style.setProperty("--sheet-width-single", `${sheetWidthSingle}px`);
      root.style.setProperty("--sheet-width-double", `${sheetWidthDouble}px`);
      root.style.setProperty("--sheet-height", `${sheetHeight}px`);
      root.style.setProperty("--sheet-pad-top", `${topPadding}px`);
      root.style.setProperty("--sheet-pad-bottom", `${bottomPadding}px`);
      root.style.setProperty("--sheet-pad-right", `${sidePadding}px`);
      root.style.setProperty("--sheet-pad-left", `${sidePadding}px`);
      root.style.setProperty("--content-height", `${contentHeight}px`);
      root.style.setProperty("--content-width", `${contentWidth}px`);
      root.style.setProperty("--lines-per-page", `${targetLinesPerPage}`);
      root.style.setProperty("--body-font-size", `${fontSize.toFixed(2)}px`);
      root.style.setProperty("--body-line-height", lineHeight.toFixed(3));
      root.style.setProperty("--line-pitch", `${linePitch.toFixed(2)}px`);
      root.style.setProperty("--body-letter-spacing", `${letterSpacingEm.toFixed(3)}em`);
    }

    function clamp(value, min, max) {
      return Math.min(Math.max(value, min), max);
    }

    function parseHashPage() {
      const raw = window.location.hash.replace(/^#/, "");
      if (!raw) {
        return 0;
      }

      const page = Number.parseInt(raw, 10);
      return Number.isNaN(page) ? 0 : Math.max(page - 1, 0);
    }

    function normalizePageIndex(index) {
      const maxIndex = Math.max(state.pages.length - 1, 0);
      let normalized = Math.min(Math.max(index, 0), maxIndex);

      if (state.spreadMode && normalized > 0 && normalized % 2 !== 0) {
        normalized -= 1;
      }

      return normalized;
    }

    function getNextIndex() {
      if (!state.spreadMode) {
        return Math.min(state.currentPageIndex + 1, state.pages.length - 1);
      }

      return Math.min(state.currentPageIndex + 2, getLastSpreadStartIndex());
    }

    function getPrevIndex() {
      if (!state.spreadMode) {
        return Math.max(state.currentPageIndex - 1, 0);
      }

      return Math.max(state.currentPageIndex - 2, 0);
    }

    function getLastSpreadStartIndex() {
      const maxIndex = Math.max(state.pages.length - 1, 0);
      return maxIndex > 0 && maxIndex % 2 !== 0 ? maxIndex - 1 : maxIndex;
    }

    function goToPage(index, updateHash = true) {
      if (!state.pages.length) {
        return;
      }

      state.currentPageIndex = normalizePageIndex(index);
      renderSpread();
      updateControls();

      if (updateHash) {
        history.replaceState(null, "", `#${state.currentPageIndex + 1}`);
      }
    }

    function updateControls() {
      const visiblePages = getVisiblePageNumbers();
      pageIndicator.textContent = visiblePages.length === 1
        ? `${visiblePages[0]} / ${state.pages.length}`
        : `${visiblePages[0]}-${visiblePages[1]} / ${state.pages.length}`;

      prevButton.disabled = state.currentPageIndex <= 0;
      nextButton.disabled = state.spreadMode
        ? state.currentPageIndex >= getLastSpreadStartIndex()
        : state.currentPageIndex >= state.pages.length - 1;
    }

    function getVisiblePageNumbers() {
      if (!state.spreadMode) {
        return [state.currentPageIndex + 1];
      }

      const leftIndex = state.currentPageIndex + 1;
      if (leftIndex < state.pages.length) {
        return [state.currentPageIndex + 1, leftIndex + 1];
      }

      return [state.currentPageIndex + 1];
    }

    function renderSpread() {
      const nodes = [];

      if (state.spreadMode) {
        nodes.push(renderSheet(state.currentPageIndex, "right"));
        nodes.push(renderSheet(state.currentPageIndex + 1, "left"));
      } else {
        nodes.push(renderSheet(state.currentPageIndex, "right"));
      }

      spreadHost.replaceChildren(...nodes);
      readerFrame.scrollTop = 0;
      readerFrame.scrollLeft = 0;
    }

    function renderSheet(pageIndex, side) {
      if (pageIndex >= state.pages.length) {
        return createBlankSheet(side);
      }

      const page = state.pages[pageIndex];
      const sheet = document.createElement("article");
      sheet.className = `sheet sheet--${side}`;

      if (page.type === "cover") {
        const cover = document.createElement("div");
        cover.className = "sheet-cover";

        const img = document.createElement("img");
        img.src = work.cover;
        img.alt = work.title + " の表紙";

        const meta = document.createElement("div");
        meta.className = "cover-meta";

        const title = document.createElement("span");
        title.textContent = work.title;

        const pageText = document.createElement("span");
        pageText.textContent = "表紙";

        meta.append(title, pageText);
        cover.append(img, meta);
        sheet.append(cover);
        return sheet;
      }

      const text = document.createElement("div");
      text.className = "sheet-text";
      renderBlocksIntoContainer(text, page.blocks);
      sheet.append(text);
      return sheet;
    }

    function createBlankSheet(side) {
      const sheet = document.createElement("article");
      sheet.className = `sheet sheet--blank sheet--${side}`;
      return sheet;
    }

    function renderBlock(block) {
      if (block.kind === "spacer") {
        const element = document.createElement("div");
        element.className = "spacer";
        return element;
      }

      const tag = /^h[1-3]$/.test(block.kind) ? block.kind : "p";
      const element = document.createElement(tag);
      element.textContent = block.text;
      return element;
    }

    function renderBlocksIntoContainer(container, blocks, isMeasure = false) {
      const inner = document.createElement("div");
      inner.className = "sheet-text-inner";
      if (isMeasure) {
        inner.dataset.measure = "true";
      }

      for (const block of blocks) {
        inner.append(renderBlock(block));
      }

      container.replaceChildren(inner);
      return inner;
    }

    function paginateWork(currentWork) {
      const pages = [{ type: "cover" }];
      const measureSheet = document.createElement("div");
      measureSheet.className = "sheet measure-sheet";

      const measureText = document.createElement("div");
      measureText.className = "sheet-text";
      measureSheet.append(measureText);
      document.body.append(measureSheet);

      let currentBlocks = [];

      for (const block of currentWork.blocks) {
        if (fitsBlocksInPage(measureText, [...currentBlocks, block])) {
          currentBlocks.push(block);
          continue;
        }

        if (currentBlocks.length > 0) {
          pages.push({ type: "text", blocks: currentBlocks });
          currentBlocks = [];
        }

        if (fitsBlocksInPage(measureText, [block])) {
          currentBlocks.push(block);
          continue;
        }

        if (block.kind === "p") {
          for (const splitText of splitParagraphAcrossPages(measureText, block.text)) {
            pages.push({ type: "text", blocks: [{ kind: "p", text: splitText }] });
          }
          continue;
        }

        pages.push({ type: "text", blocks: [block] });
      }

      if (currentBlocks.length > 0) {
        pages.push({ type: "text", blocks: currentBlocks });
      }

      measureSheet.remove();
      return pages;
    }

    function fitsBlocksInPage(measureText, blocks) {
      renderBlocksIntoContainer(measureText, blocks, true);
      return (
        measureText.scrollWidth <= measureText.clientWidth + 1 &&
        measureText.scrollHeight <= measureText.clientHeight + 1
      );
    }

    function splitParagraphAcrossPages(measureText, text) {
      const chunks = [];
      let remaining = text.trim();

      while (remaining) {
        const segment = largestFittingSegment(measureText, remaining);
        if (!segment || segment.length >= remaining.length) {
          chunks.push(remaining);
          break;
        }

        const nextRemaining = remaining.slice(segment.length).trim();
        const adjusted = rebalanceLeadingPunctuation(segment.trim(), nextRemaining);
        chunks.push(adjusted.current);
        remaining = adjusted.remaining;
      }

      return chunks.filter(Boolean);
    }

    function largestFittingSegment(measureText, text) {
      const sentenceTokens = splitIntoSentenceTokens(text);
      if (sentenceTokens.length > 1) {
        const sentenceMatch = largestFittingTokenPrefix(measureText, sentenceTokens);
        if (sentenceMatch) {
          return sentenceMatch;
        }
      }

      const charTokens = Array.from(text);
      return largestFittingTokenPrefix(measureText, charTokens) || text;
    }

    function largestFittingTokenPrefix(measureText, tokens) {
      let low = 1;
      let high = tokens.length;
      let best = "";

      while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        const candidate = tokens.slice(0, mid).join("").trim();

        if (!candidate) {
          low = mid + 1;
          continue;
        }

        if (fitsBlocksInPage(measureText, [{ kind: "p", text: candidate }])) {
          best = candidate;
          low = mid + 1;
        } else {
          high = mid - 1;
        }
      }

      return best;
    }

    function splitIntoSentenceTokens(text) {
      const rawTokens = text.match(/[^。！？!?]+[。！？!?]?["」』）】]*|.+$/gu);
      return rawTokens ? rawTokens.map((token) => token.trim()).filter(Boolean) : [text];
    }

    function rebalanceLeadingPunctuation(current, remaining) {
      if (!remaining) {
        return { current, remaining: "" };
      }

      const chars = Array.from(remaining);
      const leading = [];
      while (chars.length && "、。，．！？!?」』）】".includes(chars[0])) {
        leading.push(chars.shift());
      }

      if (leading.length === 0) {
        return { current, remaining };
      }

      return {
        current: current + leading.join(""),
        remaining: chars.join("").trimStart(),
      };
    }
  </script>
</body>
</html>
"""

    return (
        template.replace("__TITLE__", escape(title))
        .replace("__SOCIAL_META__", meta_tags)
        .replace("__FOLDER__", escape(folder_name))
        .replace("__COVER__", escape(cover_filename))
        .replace("__BLOCKS_JSON__", blocks_json)
        .replace("__READER_CONFIG__", reader_config_json)
        .replace("__BODY_FONT_MAX__", str(DEFAULT_BODY_FONT_MAX_PX))
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
        cover = f"{escape(work.folder)}/{escape(work.cover)}"
        cards.append(
            f"""
      <a class="card" href="{href}">
        <div class="card-cover">
          <img src="{cover}" alt="{escape(work.title)} の表紙" loading="lazy">
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
