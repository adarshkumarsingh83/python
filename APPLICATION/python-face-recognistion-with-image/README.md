# Python Face Recognition with Image

A small proof-of-concept that uses the [`face_recognition`](https://github.com/ageitgey/face_recognition) library (built on top of dlib) and OpenCV to:

1. **Compare two still images** and decide whether they show the same person.
2. **Recognize a known face live from your webcam** and draw a labelled box around it.

---

## Project structure

| File | Purpose |
|------|---------|
| [image_to_image.py](image_to_image.py) | Compares a known image against an unknown image and prints whether they match. |
| [image_to_video.py](image_to_video.py) | Opens the webcam, detects faces in each frame, and labels the known person in real time. |
| [requirements.txt](requirements.txt) | Python dependencies. |
| [adarsh.jpg](adarsh.jpg) | Sample known/reference face image. |

---

## How it works

Both scripts rely on the same underlying pipeline from `face_recognition`:

1. **Load image** – `face_recognition.load_image_file(path)` reads an image into a NumPy array (RGB).
2. **Encode face** – `face_recognition.face_encodings(image)` returns a list of 128-dimensional embeddings, one per face found. `[0]` takes the first face.
3. **Compare** – `face_recognition.compare_faces([known], unknown, tolerance=0.6)` returns a list of booleans. A lower `tolerance` is stricter (default `0.6`).

### `image_to_image.py` — still image comparison

```
load known image ──► encode known face
load unknown image ─► encode unknown face ──► compare_faces() ──► print "Match" / "No Match"
```

- Catches `IndexError` so it prints a friendly message if no face is found in either image.
- **Note:** this script currently points at `./img/adarsh.jpg` and `./img/random.jpg`. Those paths don't exist in the repo yet — see [Adjusting image paths](#adjusting-image-paths) below.

### `image_to_video.py` — live webcam recognition

```
encode known face (adarsh.jpg)
        │
        ▼
open webcam ──► read frame ──► BGR→RGB ──► find faces + encodings
        ▲                                          │
        │                                          ▼
        │                        for each face: compare to known
        │                                          │
        └──────── draw box + name label ◄──────────┘
        │
   show window  ──►  press 'q' to quit  ──►  release camera + close windows
```

- Uses `cv2.VideoCapture(0)` (default camera).
- Converts each frame from OpenCV's BGR to RGB (what `face_recognition` expects).
- Draws a green rectangle and a name label (`"Your Name"` for a match, `"Unknown"` otherwise).
- Press **`q`** in the video window to exit.

---

## Prerequisites

- **Python 3.x** (tested on Python 3.14).
- A C/C++ build toolchain (dlib compiles native code). On macOS install Xcode Command Line Tools:
  ```bash
  xcode-select --install
  ```
- A working **webcam** for `image_to_video.py`.

---

## Installation

```bash
# (recommended) create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# install dependencies
pip install -r requirements.txt
```

> **Why `setuptools<81`?** `face_recognition_models` imports `pkg_resources`, which
> was **removed from setuptools 81+**. On newer Python (3.12+) setuptools is no longer
> bundled, so without this pin you get a misleading error:
> *"Please install `face_recognition_models`…"* even when it's already installed.
> The pin in `requirements.txt` keeps `pkg_resources` available.

If you prefer to install the models package directly from source instead of via pip:

```bash
pip install git+https://github.com/ageitgey/face_recognition_models
```

---

## Running

### 1. Live webcam recognition

```bash
python3 image_to_video.py
```

- On macOS the first run triggers a **Camera permission** prompt for your terminal/IDE.
  Allow it (System Settings → Privacy & Security → Camera), otherwise frames come back
  empty and the program exits immediately.
- A window titled **"Video Face Recognition"** appears. Press **`q`** to quit.

### 2. Still image comparison

```bash
python3 image_to_image.py
```

Prints one of:
- `Match Found! This is the known person.`
- `No Match. This is a different person.`
- `No faces were detected in one of the images.`

---

## Adjusting image paths

`image_to_image.py` references `./img/adarsh.jpg` and `./img/random.jpg`. To run it against the
files in this repo, either:

- **Option A** – edit the paths in the script to `"adarsh.jpg"` and your second image, or
- **Option B** – create an `img/` folder and place `adarsh.jpg` and `random.jpg` inside it:
  ```bash
  mkdir -p img
  cp adarsh.jpg img/adarsh.jpg
  # add a second photo as img/random.jpg
  ```

To recognize **your own** face in the webcam script, replace `adarsh.jpg` with a clear,
front-facing photo of yourself and update `known_face_names = ["Your Name"]` in
[image_to_video.py](image_to_video.py).

---

## Troubleshooting

| Symptom | Cause / Fix |
|---------|-------------|
| `Please install face_recognition_models…` (but it's installed) | Missing `pkg_resources`. Run `pip install "setuptools<81"`. |
| `ModuleNotFoundError: No module named 'pkg_resources'` | Same as above — setuptools 81+ removed it. |
| dlib fails to build during install | Install a compiler (Xcode CLT on macOS / build-essential + cmake on Linux). |
| Webcam window is black / program exits instantly | Grant camera permission, or another app is using the camera. |
| `IndexError` / "No faces were detected" | The image has no detectable face — use a clearer, front-facing photo. |
