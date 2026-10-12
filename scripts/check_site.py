"""Validate catalog links and reader resources through a temporary HTTP server."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from urllib.parse import quote
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


def main():
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    origin = f"http://127.0.0.1:{server.server_port}/"

    def fetch(path):
        with urlopen(origin + quote(path, safe="/?=&"), timeout=10) as response:
            assert response.status == 200, path
            data = response.read()
            assert data, f"Empty resource: {path}"
            return data

    try:
        catalog = fetch("index.html").decode("utf-8")
        reader = fetch("book.html").decode("utf-8")
        assert "doc.md" in reader and "title.jpg" in reader
        works = sorted(path for path in ROOT.iterdir() if path.is_dir() and (path / "doc.md").is_file())
        assert works, "No stories found"
        for work in works:
            folder = quote(work.name, safe="")
            assert f"{folder}/" in catalog or f"{work.name}/" in catalog, work.name
            wrapper = fetch(f"{work.name}/index.html").decode("utf-8")
            assert f"book={folder}" in wrapper or f"book={work.name}" in wrapper, work.name
            fetch(f"{work.name}/doc.md").decode("utf-8")
            image = fetch(f"{work.name}/title.jpg")
            assert image.startswith(b"\xff\xd8"), f"Invalid JPEG: {work.name}"
        print(f"HTTP resources OK: {len(works)} stories, catalog and shared reader")
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


if __name__ == "__main__":
    main()
