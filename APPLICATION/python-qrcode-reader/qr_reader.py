#!/usr/bin/env python3
"""QR code reader.

Decode QR codes from an image file or a live webcam stream using OpenCV's
built-in QRCodeDetector (no native zbar dependency required).

Usage:
    python qr_reader.py image path/to/qr.png
    python qr_reader.py image path/to/qr.png --json
    python qr_reader.py webcam
    python qr_reader.py webcam --camera 1
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, asdict
from typing import List, Optional

import cv2
import numpy as np


@dataclass
class QRResult:
    """A single decoded QR code and where it was found in the image."""

    data: str
    # Bounding-box corner points as (x, y) integer pairs, clockwise from top-left.
    points: List[List[int]]


def _points_to_list(points: Optional[np.ndarray]) -> List[List[int]]:
    if points is None:
        return []
    return [[int(x), int(y)] for x, y in points.reshape(-1, 2)]


def decode_image(image: np.ndarray) -> List[QRResult]:
    """Detect and decode every QR code present in a BGR image array."""
    detector = cv2.QRCodeDetector()

    # detectAndDecodeMulti handles one or many codes in a single frame.
    ok, decoded, points, _ = detector.detectAndDecodeMulti(image)
    results: List[QRResult] = []
    if ok and decoded is not None:
        for text, pts in zip(decoded, points):
            if text:  # skip detections that could not be decoded
                results.append(QRResult(data=text, points=_points_to_list(pts)))

    # Fall back to single-code decode if the multi pass found nothing.
    if not results:
        text, pts, _ = detector.detectAndDecode(image)
        if text:
            results.append(QRResult(data=text, points=_points_to_list(pts)))

    return results


def read_from_file(path: str) -> List[QRResult]:
    """Load an image from disk and decode any QR codes within it."""
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Could not read image: {path}")
    return decode_image(image)


def read_from_webcam(camera_index: int = 0) -> Optional[QRResult]:
    """Open a webcam window and return the first QR code decoded.

    Press 'q' or Esc to quit without decoding.
    """
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open camera index {camera_index}")

    detector = cv2.QRCodeDetector()
    found: Optional[QRResult] = None
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            text, pts, _ = detector.detectAndDecode(frame)
            if text and pts is not None:
                box = np.int32(pts).reshape(-1, 2)
                cv2.polylines(frame, [box], True, (0, 255, 0), 3)
                cv2.putText(
                    frame, text, tuple(box[0]),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2,
                )
                found = QRResult(data=text, points=_points_to_list(pts))

            cv2.imshow("QR Reader (press q to quit)", frame)
            key = cv2.waitKey(1) & 0xFF
            if key in (ord("q"), 27) or found is not None:
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

    return found


def _print_results(results: List[QRResult], as_json: bool) -> None:
    if as_json:
        print(json.dumps([asdict(r) for r in results], indent=2))
        return
    if not results:
        print("No QR code found.")
        return
    for i, r in enumerate(results, 1):
        print(f"[{i}] {r.data}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Read QR codes from an image or webcam.")
    sub = parser.add_subparsers(dest="command", required=True)

    img = sub.add_parser("image", help="Decode QR codes from an image file")
    img.add_argument("path", help="Path to the image file")
    img.add_argument("--json", action="store_true", help="Output results as JSON")

    cam = sub.add_parser("webcam", help="Decode QR codes from a live webcam")
    cam.add_argument("--camera", type=int, default=0, help="Camera index (default: 0)")
    cam.add_argument("--json", action="store_true", help="Output result as JSON")

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "image":
        try:
            results = read_from_file(args.path)
        except FileNotFoundError as e:
            print(e, file=sys.stderr)
            return 1
        _print_results(results, args.json)
        return 0 if results else 2

    if args.command == "webcam":
        try:
            result = read_from_webcam(args.camera)
        except RuntimeError as e:
            print(e, file=sys.stderr)
            return 1
        _print_results([result] if result else [], args.json)
        return 0 if result else 2

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
