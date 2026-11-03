"""Restore JPEG covers for November 3 shorts from source SVG artwork.

The site's canonical published cover format is title.jpg. The SVG drawings are
source artwork only; the shared reader and generator remain JPEG-first.
"""
from io import BytesIO
from pathlib import Path
import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

def main():
    for folder in sorted(ROOT.glob("20261103-*")):
        svg = folder / "title.svg"
        if not svg.is_file():
            continue
        png = cairosvg.svg2png(bytestring=svg.read_bytes(), output_width=720, output_height=960)
        with Image.open(BytesIO(png)) as im:
            im.convert("RGB").save(folder / "title.jpg", "JPEG",
                                   quality=86, subsampling=0, optimize=True)
        print("Wrote", folder / "title.jpg")

if __name__ == "__main__":
    main()
