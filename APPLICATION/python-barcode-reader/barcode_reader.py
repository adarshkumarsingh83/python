"""Barcode reader.

Reads (decodes) barcodes from image files and prints the decoded data to the
console. Built on top of `pyzbar` (a Python wrapper around the `zbar` C
library) with Pillow for image loading.

Usage examples
--------------
Read a single image::

    python barcode_reader.py resources/demo_ean13.png

Read several images at once::

    python barcode_reader.py resources/demo_ean13.png resources/demo_code128.png

Read every PNG in the resources/ directory (no arguments)::

    python barcode_reader.py

System requirements
-------------------
`pyzbar` needs the native `zbar` shared library:

    macOS:          brew install zbar
    Debian/Ubuntu:  sudo apt-get install libzbar0
    Windows:        bundled with the pyzbar wheel

On Apple-Silicon macOS the Homebrew library lives in ``/opt/homebrew/lib``,
which Python's ``ctypes`` does not search by default. :func:`_ensure_zbar`
patches the library lookup so no manual ``DYLD_LIBRARY_PATH`` is required.
"""

from __future__ import annotations

import argparse
import ctypes.util
import glob
import os
import sys

RESOURCES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources")


def _ensure_zbar() -> None:
    """Make the Homebrew ``zbar`` library discoverable on macOS.

    ``pyzbar`` resolves the native library through
    ``ctypes.util.find_library('zbar')``, which does not look in the Homebrew
    directories (``/opt/homebrew/lib`` on Apple Silicon, ``/usr/local/lib`` on
    Intel). We wrap that lookup so importing ``pyzbar`` works out of the box.
    """
    if sys.platform != "darwin":
        return

    original = ctypes.util.find_library

    def patched(name: str):
        if name == "zbar":
            for directory in ("/opt/homebrew/lib", "/usr/local/lib"):
                hits = sorted(glob.glob(os.path.join(directory, "libzbar*.dylib")))
                if hits:
                    return hits[-1]
        return original(name)

    ctypes.util.find_library = patched


_ensure_zbar()

try:
    from PIL import Image
    from pyzbar.pyzbar import decode
except ImportError as exc:  # pragma: no cover - dependency / system lib missing
    print(
        "Error: failed to import dependencies.\n"
        f"  {exc}\n\n"
        "Make sure the Python packages and the native zbar library are installed:\n"
        "  pip install -r requirements.txt\n"
        "  macOS:         brew install zbar\n"
        "  Debian/Ubuntu: sudo apt-get install libzbar0",
        file=sys.stderr,
    )
    raise SystemExit(1)


def read_barcodes(image_path: str) -> list[dict]:
    """Decode every barcode found in ``image_path``.

    Returns a list of dicts with ``type`` and ``data`` keys (one entry per
    barcode detected in the image).
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(image_path)

    results = decode(Image.open(image_path))
    return [
        {"type": r.type, "data": r.data.decode("utf-8", errors="replace")}
        for r in results
    ]


def _collect_default_images() -> list[str]:
    """Return all PNG images in the resources directory (sorted)."""
    return sorted(glob.glob(os.path.join(RESOURCES_DIR, "*.png")))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Read barcodes from image files and print the results.",
    )
    parser.add_argument(
        "images",
        nargs="*",
        help="Image file(s) to read. Defaults to every PNG in resources/.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    images = args.images or _collect_default_images()
    if not images:
        print(f"No images to read (none given and none found in {RESOURCES_DIR}).")
        return 1

    total = 0
    for image_path in images:
        try:
            found = read_barcodes(image_path)
        except FileNotFoundError:
            print(f"{image_path}: file not found", file=sys.stderr)
            continue

        if not found:
            print(f"{image_path}: no barcode detected")
            continue

        for item in found:
            total += 1
            print(f"{image_path}: [{item['type']}] {item['data']}")

    print(f"\nDecoded {total} barcode(s) from {len(images)} image(s).")
    return 0 if total else 1


if __name__ == "__main__":
    raise SystemExit(main())
