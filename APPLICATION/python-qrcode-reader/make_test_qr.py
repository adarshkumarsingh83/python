#!/usr/bin/env python3
"""Generate a QR code image for testing the reader.

Usage:
    python make_test_qr.py "text or URL" output.png
"""
import sys

import qrcode


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 1
    data, out_path = sys.argv[1], sys.argv[2]
    img = qrcode.make(data)
    img.save(out_path)
    print(f"Wrote {out_path} encoding: {data!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
