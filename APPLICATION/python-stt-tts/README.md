# python-stt-tts

Free, **offline** speech examples in Python — no internet connection and no API keys required.

| Capability | Library | Notes |
|------------|---------|-------|
| **TTS** — Text-to-Speech | [pyttsx3](https://pypi.org/project/pyttsx3/) | Speaks text aloud using your OS's built-in voices |
| **STT** — Speech-to-Text | [Vosk](https://alphacephei.com/vosk/) | Live transcription from the microphone |

Both run entirely on your machine.

## Requirements

- Python 3.x
- A working microphone (for STT) and speakers (for TTS)

## Installation

Install the Python packages:

```bash
pip install -r requirements.txt
```

Or install them individually:

```bash
pip install pyttsx3 vosk sounddevice
```

### Linux-only system dependencies

`pyttsx3` needs `espeak`, and `sounddevice` needs PortAudio:

```bash
sudo apt install espeak libportaudio2
```

> On **macOS** and **Windows**, the system speech engine and audio backend are already available, so no extra system packages are needed.

### Download a Vosk model (required for STT)

Download a model from <https://alphacephei.com/vosk/models> and unzip it **next to this script**.

The examples default to the small English model:

```
vosk-model-small-en-us-0.15   (~50 MB)
```

After unzipping, the folder layout should look like:

```
python-stt-tts/
├── speech_examples.py
└── vosk-model-small-en-us-0.15/
    ├── am/
    ├── conf/
    └── ...
```

## Usage

```bash
# Speak a sentence out loud
python speech_examples.py tts

# Listen and transcribe live from the microphone (Ctrl+C to stop)
python speech_examples.py stt
```

Running with no argument (or an unrecognized one) prints the usage message.

## How it works

### Text-to-Speech ([`text_to_speech()`](speech_examples.py#L31))

Uses `pyttsx3` to synthesize speech locally. You can tune:

- **rate** — speaking speed in words per minute (default `175`)
- **volume** — `0.0` to `1.0` (default `1.0`)
- **voice** — pick a different installed voice (commented example in the code)

To **save to a WAV file** instead of speaking aloud, use `engine.save_to_file(text, "output.wav")` (see the commented snippet in the source).

### Speech-to-Text ([`speech_to_text()`](speech_examples.py#L53))

Uses Vosk with a 16 kHz mono audio stream captured via `sounddevice`:

- Audio is captured in a background callback and pushed onto a queue.
- `KaldiRecognizer` consumes the audio and emits:
  - **partial** results (words recognized so far, printed inline with `...`)
  - **full** phrase results (printed as `You said: ...`)
- Press **Ctrl+C** to stop listening.

If the Vosk model can't be found at the given path, the script exits with a hint pointing to the model download page.

## Project structure

```
python-stt-tts/
├── speech_examples.py   # TTS + STT examples with a small CLI
├── requirements.txt     # Python dependencies
└── README.md
```

## Troubleshooting

- **`Could not load Vosk model ...`** — Make sure you downloaded and unzipped a Vosk model, and that its folder name matches the `model_path` (default `vosk-model-small-en-us-0.15`).
- **No audio / PortAudio errors (Linux)** — Install `libportaudio2` (see above) and confirm your microphone is detected.
- **No voice / silent TTS (Linux)** — Install `espeak`.
