"""Barcode generator.

Generates barcodes in various symbologies (Code128, Code39, EAN-13, EAN-8,
UPC-A, ISBN-13, ...) and saves them as PNG images into the ``resources``
directory.

Usage examples
--------------
Generate a default Code128 barcode::

    python barcode_generator.py "Hello-12345"

Generate an EAN-13 barcode with a custom file name::

    python barcode_generator.py 5901234123457 --type ean13 --name my_product

List every supported barcode type::

    python barcode_generator.py --list

Run the bundled demo (one sample per common type)::

    python barcode_generator.py --demo
"""

from __future__ import annotations

import argparse
import os
import sys

import barcode
from barcode.writer import ImageWriter

# Directory where every generated barcode image is stored.
RESOURCES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources")

# A few well-known, valid sample payloads used by ``--demo``.
# Note: checksum based symbologies (ean13, ean8, upca, ...) require numeric
# input of a specific length.
DEMO_SAMPLES = {
    "code128": "CODE128-DEMO-001",
    "code39": "CODE39DEMO",
    "ean13": "5901234123457",
    "ean8": "96385074",
    "upca": "036000291452",
    "isbn13": "9781492056355",
}


def supported_types() -> list[str]:
    """Return the sorted list of symbologies provided by python-barcode."""
    return sorted(barcode.PROVIDED_BARCODES)


def generate(data: str, code_type: str = "code128", name: str | None = None) -> str:
    """Generate a single barcode image and save it under ``resources``.

    Parameters
    ----------
    data:
        The payload to encode.
    code_type:
        One of :func:`supported_types` (e.g. ``code128``, ``ean13``).
    name:
        Base file name (without extension). Defaults to ``<code_type>_<data>``.

    Returns
    -------
    str
        The absolute path of the written PNG file.
    """
    if code_type not in barcode.PROVIDED_BARCODES:
        raise ValueError(
            f"Unsupported barcode type {code_type!r}. "
            f"Choose one of: {', '.join(supported_types())}"
        )

    os.makedirs(RESOURCES_DIR, exist_ok=True)

    if name is None:
        # Build a filesystem-friendly default name from the data.
        safe = "".join(c if c.isalnum() else "_" for c in data)
        name = f"{code_type}_{safe}"

    barcode_class = barcode.get_barcode_class(code_type)
    code = barcode_class(data, writer=ImageWriter())

    # ``save`` appends the ``.png`` extension automatically.
    output_base = os.path.join(RESOURCES_DIR, name)
    saved_path = code.save(output_base)
    return os.path.abspath(saved_path)


def run_demo() -> list[str]:
    """Generate one barcode for each entry in :data:`DEMO_SAMPLES`."""
    written = []
    for code_type, data in DEMO_SAMPLES.items():
        path = generate(data, code_type=code_type, name=f"demo_{code_type}")
        written.append(path)
        print(f"  [{code_type:8}] {data:16} -> {path}")
    return written


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate barcodes and save them as PNG files in resources/.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("data", nargs="?", help="The data to encode in the barcode.")
    parser.add_argument(
        "-t",
        "--type",
        default="code128",
        help="Barcode symbology (default: code128). Use --list to see all options.",
    )
    parser.add_argument(
        "-n",
        "--name",
        default=None,
        help="Output file name without extension (default: <type>_<data>).",
    )
    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="List all supported barcode types and exit.",
    )
    parser.add_argument(
        "-d",
        "--demo",
        action="store_true",
        help="Generate a sample barcode for each common type.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.list:
        print("Supported barcode types:")
        for name in supported_types():
            print(f"  - {name}")
        return 0

    if args.demo:
        print("Generating demo barcodes:")
        run_demo()
        return 0

    if not args.data:
        parser.error("the 'data' argument is required (or use --demo / --list)")

    try:
        path = generate(args.data, code_type=args.type, name=args.name)
    except Exception as exc:  # noqa: BLE001 - surface a friendly message
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Barcode saved to: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
