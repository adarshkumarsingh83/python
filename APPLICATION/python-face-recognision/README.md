# Python Face Recognition Tool

A simple face detection and data-collection tool built with Python and OpenCV, based on the GeeksforGeeks tutorial [Build Your Own Face Recognition Tool With Python](https://www.geeksforgeeks.org/python/build-your-own-face-recognition-tool-with-python/).

The program works like a smart camera: it reads frames from your webcam, detects frontal faces in real time using a pre-trained Haar Cascade classifier, draws bounding boxes around them, and collects cropped face images that can later be used to train a recognition model.

## Features

- Real-time face detection from your webcam
- Pre-trained Haar Cascade frontal-face classifier (no training required to detect)
- Selective sampling of face images (every 10th frame, up to 100 samples) to avoid redundant near-identical frames
- On-screen overlay showing the live sample count and a red bounding box around each detected face

## How It Works

The tool processes the video feed frame by frame:

1. **Capture** – `cv2.VideoCapture(0)` opens the default webcam (use `1` or `2` for alternate cameras).
2. **Load classifier** – `cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')` loads the pre-trained model.
3. **Grayscale conversion** – each frame is converted to grayscale to make detection faster and easier.
4. **Detection** – `detectMultiScale(gray, 1.3, 5)` locates faces, returning their `(x, y, w, h)` bounding boxes.
5. **Crop & resize** – each detected face is cropped and resized to a standard `50×50` pixels.
6. **Selective storage** – a face is saved to `faces_data` only when fewer than 100 samples have been collected *and* the frame counter is divisible by 10, so the dataset stays varied.
7. **Display** – the current sample count and a red rectangle are drawn on the frame, which is shown in a window.
8. **Exit & cleanup** – press `q` to stop; the camera is released with `video.release()` and windows closed with `cv2.destroyAllWindows()`.

## Requirements

- Python 3.x
- A working webcam
- [OpenCV](https://pypi.org/project/opencv-python/) and [NumPy](https://pypi.org/project/numpy/)
- The Haar Cascade file `data/haarcascade_frontalface_default.xml` (included in this repo)

## Installation

Install the dependencies using the requirements file:

```
pip install -r requirements.txt
```

Or install them individually:

```
pip install opencv-python
pip install numpy
```

## Usage

Run the script:

```
python main.py
```

A window opens showing your webcam feed. Each detected face is outlined with a red rectangle, and a counter in the top-left shows how many face samples have been collected. Press **`q`** to quit.

## Project Structure

```
python-face-recognision/
├── main.py                                   # Face detection & data collection script
├── requirements.txt                          # Python dependencies (opencv-python, numpy)
├── data/
│   └── haarcascade_frontalface_default.xml   # Pre-trained Haar Cascade classifier
└── README.md
```

## Next Steps

The collected face samples are the first stage of a full recognition pipeline. To extend this into a complete face-recognition tool, you can:

- Persist the collected `faces_data` (e.g. with `pickle`) along with a label/name for each person
- Train a classifier such as **K-Nearest Neighbors (KNN)** on the stored samples
- Run live recognition by matching newly detected faces against the trained model

## Reference

- [GeeksforGeeks – Build Your Own Face Recognition Tool With Python](https://www.geeksforgeeks.org/python/build-your-own-face-recognition-tool-with-python/)
