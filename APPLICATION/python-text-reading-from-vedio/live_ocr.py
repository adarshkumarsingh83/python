"""
Read text from a live webcam video stream using OpenCV + Tesseract OCR.

Setup
-----
1. Install the Tesseract OCR engine (the actual binary, not just the Python wrapper):
     - macOS:   brew install tesseract
     - Ubuntu:  sudo apt install tesseract-ocr
     - Windows: https://github.com/UB-Mannheim/tesseract/wiki

2. Install the Python dependencies:
     pip install opencv-python pytesseract

Run
---
     python live_ocr.py

Controls
--------
     q  -> quit
     s  -> save the current frame (with detected boxes) to disk
"""

import cv2
import pytesseract
from pytesseract import Output

# If Tesseract is not on your PATH, point to it explicitly, e.g.:
# pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Only draw/print words Tesseract is at least this confident about (0-100).
MIN_CONFIDENCE = 60

# OCR is expensive; run it every Nth frame to keep the preview smooth.
OCR_EVERY_N_FRAMES = 5


def preprocess(frame):
    """Convert a frame to a cleaner black-and-white image for better OCR."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Adaptive threshold copes with uneven lighting better than a fixed one.
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 15
    )
    return thresh


def run_ocr(frame):
    """Return a list of (text, confidence, (x, y, w, h)) for detected words."""
    processed = preprocess(frame)
    data = pytesseract.image_to_data(processed, output_type=Output.DICT)

    results = []
    for i in range(len(data["text"])):
        text = data["text"][i].strip()
        conf = int(float(data["conf"][i])) if data["conf"][i] != "-1" else -1
        if text and conf >= MIN_CONFIDENCE:
            box = (
                data["left"][i],
                data["top"][i],
                data["width"][i],
                data["height"][i],
            )
            results.append((text, conf, box))
    return results


def draw_results(frame, results):
    """Draw bounding boxes and the recognized text onto the frame."""
    for text, conf, (x, y, w, h) in results:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            text,
            (x, y - 8),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2,
        )
    return frame


def main():
    cap = cv2.VideoCapture(0)  # 0 = default camera
    if not cap.isOpened():
        raise RuntimeError("Could not open the camera. Is it connected / permitted?")

    frame_count = 0
    last_results = []

    print("Reading text from camera. Press 'q' to quit, 's' to save a frame.")
    while True:
        ok, frame = cap.read()
        if not ok:
            print("Failed to grab a frame.")
            break

        # Run OCR only periodically, but keep drawing the latest result every frame.
        if frame_count % OCR_EVERY_N_FRAMES == 0:
            last_results = run_ocr(frame)
            recognized = " ".join(text for text, _, _ in last_results)
            if recognized:
                print("Detected:", recognized)

        draw_results(frame, last_results)
        cv2.imshow("Live OCR (press q to quit)", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        if key == ord("s"):
            cv2.imwrite("captured_frame.png", frame)
            print("Saved captured_frame.png")

        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
