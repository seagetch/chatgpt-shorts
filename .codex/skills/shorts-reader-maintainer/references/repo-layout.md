# Repo Layout

## Core files

- `book.html`
  - Shared runtime reader.
  - Loads `./<book>/doc.md` and `./<book>/title.jpg`.
  - Owns pagination, spread layout, controls, swipe, and font-loading behavior.

- `generate_reader.py`
  - Generates each work folder `index.html`.
  - Generates the root `index.html` catalog.
  - Converts `title.png` to `title.jpg`.
  - Emits social-card metadata using `SITE_URL`.

- `index.html`
  - Root catalog page generated from subfolders.

## Work folders

Each story folder is expected to contain:

- `doc.md` - markdown source
- `title.png` - editable cover source
- `title.jpg` - generated cover used by the site
- `index.html` - generated redirect wrapper

## Expected validation flow

1. Edit `book.html` or `generate_reader.py`.
2. If `generate_reader.py` changed, run:
   - `python -m py_compile generate_reader.py`
   - `python generate_reader.py`
3. Serve the repo over HTTP:
   - `python -m http.server`
4. Verify:
   - root catalog
   - one work page through its folder `index.html`
   - direct shared reader URL `book.html?book=<folder>`
