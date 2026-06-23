#!/usr/bin/env python3
"""Generate a QR code from console input.

Prompts for the data to encode and a file name, then writes the QR code
image into the ``resources/`` directory next to this script.

Usage:
    python qr_generator.py
        -> prompts interactively for data and file name

    python qr_generator.py "https://example.com" adarsh
        -> non-interactive; writes resources/adarsh.png
"""
from __future__ import annotations

import os
import re
import sys
from typing import Optional

import qrcode

RESOURCES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources")


def _sanitize_name(name: str) -> str:
    """Turn a user-supplied name into a safe .png file name."""
    name = name.strip()
    if not name:
        raise ValueError("File name cannot be empty.")
    # Drop any directory components and keep a conservative character set.
    base = os.path.basename(name)
    base = re.sub(r"\.png$", "", base, flags=re.IGNORECASE)
    base = re.sub(r"[^A-Za-z0-9._-]", "_", base)
    if not base:
        raise ValueError("File name has no usable characters.")
    return base + ".png"


def generate_qr(data: str, file_name: str) -> str:
    """Encode ``data`` as a QR code and save it under ``resources/``.

    Returns the full path of the written image.
    """
    if not data.strip():
        raise ValueError("Data to encode cannot be empty.")

    os.makedirs(RESOURCES_DIR, exist_ok=True)
    out_path = os.path.join(RESOURCES_DIR, _sanitize_name(file_name))

    qr = qrcode.QRCode(
        version=None,  # auto-size to fit the data
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(out_path)
    return out_path


def main(argv: Optional[list[str]] = None) -> int:
    argv = sys.argv[1:] if argv is None else argv

    if len(argv) >= 2:
        data, file_name = argv[0], argv[1]
    else:
        try:
            data = input("Enter the text or URL to encode: ").strip()
            file_name = input("Enter the output file name (e.g. adarsh): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nCancelled.", file=sys.stderr)
            return 1

    try:
        out_path = generate_qr(data, file_name)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    print(f"QR code saved to: {out_path}")
    print(f"Encoded data:     {data!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
