# Live Video Text Reader (OCR)

Read text from a **live webcam video stream** in real time using [OpenCV](https://opencv.org/) for video capture and [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for text recognition.

The script grabs frames from your camera, runs OCR on them, draws bounding boxes around detected words, and prints the recognized text to the console.

---

## Demo / What it does

- Opens your default camera and shows a live preview window.
- Detects words in each frame and draws a green box + red label around them.
- Prints recognized text to the terminal.
- Lets you save the current frame to disk.

---

## Requirements

| Component | Why it's needed |
|-----------|-----------------|
| Python 3.7+ | Runs the script |
| [Tesseract OCR engine](https://github.com/tesseract-ocr/tesseract) | The actual OCR engine (a native binary) |
| `opencv-python` | Camera capture + image processing |
| `pytesseract` | Python wrapper that calls Tesseract |
| A working webcam | Video input |

> **Important:** `pytesseract` is only a wrapper. You must install the **Tesseract engine** separately (see below).

---

## Installation

### 1. Install the Tesseract OCR engine

**macOS (Homebrew):**
```bash
brew install tesseract
```

**Ubuntu / Debian:**
```bash
sudo apt update
sudo apt install tesseract-ocr
```

**Windows:**
Download and run the installer from the
[UB Mannheim Tesseract page](https://github.com/UB-Mannheim/tesseract/wiki).
Note the install path (e.g. `C:\Program Files\Tesseract-OCR\tesseract.exe`).

Verify the install:
```bash
tesseract --version
```

### 2. Install the Python dependencies

The dependencies are pinned in [requirements.txt](requirements.txt). Install them with:

```bash
pip install -r requirements.txt
```

> Tip: use a virtual environment to keep things isolated:
> ```bash
> python -m venv .venv
> source .venv/bin/activate      # Windows: .venv\Scripts\activate
> pip install -r requirements.txt
> ```

Or install them directly:
```bash
pip install opencv-python pytesseract
```

### 3. (If needed) Point pytesseract at the Tesseract binary

If you get a `TesseractNotFoundError`, the engine isn't on your `PATH`.
Open [live_ocr.py](live_ocr.py) and uncomment / edit the line near the top:

```python
# macOS (Apple Silicon, Homebrew):
pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"

# macOS (Intel, Homebrew):
# pytesseract.pytesseract.tesseract_cmd = r"/usr/local/bin/tesseract"

# Windows:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## Usage

```bash
python live_ocr.py
```

### Controls

| Key | Action |
|-----|--------|
| `q` | Quit the program |
| `s` | Save the current frame (with boxes) to `captured_frame.png` |

On **macOS**, the first run triggers a **camera permission** prompt — allow access for your terminal or IDE, otherwise the camera won't open.

---

## Configuration

Tweak these constants at the top of [live_ocr.py](live_ocr.py):

| Constant | Default | Description |
|----------|---------|-------------|
| `MIN_CONFIDENCE` | `60` | Minimum Tesseract confidence (0–100) for a word to be shown. Lower = more (noisier) text; higher = stricter. |
| `OCR_EVERY_N_FRAMES` | `5` | Run OCR every Nth frame. OCR is slow, so this keeps the preview smooth. Lower = more responsive but heavier. |

---

## How it works

1. **Capture** — `cv2.VideoCapture(0)` opens the default camera (`0`). Change the index for other cameras.
2. **Preprocess** — `preprocess()` converts each frame to grayscale and applies an **adaptive threshold**, which handles uneven lighting far better than a fixed threshold and improves OCR accuracy.
3. **Recognize** — `run_ocr()` calls `pytesseract.image_to_data()`, which returns every detected word along with its **confidence** and **bounding box**. Low-confidence and empty results are filtered out.
4. **Display** — `draw_results()` overlays green boxes and red text labels onto the live frame, shown via `cv2.imshow()`.
5. **Throttle** — OCR runs only every `OCR_EVERY_N_FRAMES` frames; the last result is re-drawn on intermediate frames so the video stays smooth.

---

## Project structure

```
python-text-reading-from-vedio/
├── live_ocr.py         # Main script: capture + OCR + display
├── requirements.txt    # Python dependencies (pip install -r)
└── README.md           # This file
```

---

## Troubleshooting

| Problem | Likely cause / fix |
|---------|--------------------|
| `Could not open the camera` | Camera in use by another app, no camera connected, or OS permission denied. |
| `TesseractNotFoundError` | Tesseract engine not installed or not on `PATH`. Install it, or set `tesseract_cmd` (see step 3). |
| Black or frozen window | Camera permission not granted (macOS), or wrong camera index — try `cv2.VideoCapture(1)`. |
| No / poor text detected | Improve lighting, hold text steady & flat, increase camera resolution, or lower `MIN_CONFIDENCE`. |
| Laggy preview | Increase `OCR_EVERY_N_FRAMES`, or reduce the frame resolution. |
| Garbled characters | Tesseract struggles with stylized fonts, angles, and motion blur — get the text square-on and well-lit. |

---

## Possible improvements

- **Log to a file** — append recognized text with timestamps to a `.txt`/`.csv`.
- **Read from a video file** instead of a camera: `cv2.VideoCapture("video.mp4")`.
- **Other languages** — install language packs (e.g. `tesseract-ocr-hin`) and pass `lang="hin"` to `image_to_data`.
- **EasyOCR / PaddleOCR** — deep-learning OCR with no native binary; often better for non-Latin scripts and tilted text.
- **GPU acceleration** for higher frame rates.

---

## License

Free to use and modify for your own projects.
