# python-stt-tts-wireless

Free, **offline** speech examples in Python — no internet connection and no API keys required.

| Capability | Library | Notes |
|------------|---------|-------|
| **TTS** — Text-to-Speech | [pyttsx3](https://pypi.org/project/pyttsx3/) | Speaks text aloud using your OS's built-in voices |
| **STT** — Speech-to-Text | [Vosk](https://alphacephei.com/vosk/) | Live transcription from the microphone |
| **Echo** — Listen + repeat | Vosk + TTS | Transcribes what you say and speaks it back, in a loop |

Everything runs entirely on your machine.

## Requirements

- Python 3.x
- A working microphone (for STT/echo) and speakers (for TTS/echo)

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

> On **macOS** and **Windows**, the system speech engine and audio backend are already available, so no extra system packages are needed. On macOS the echo mode uses the built-in `say` command when available.

### Download a Vosk model (required for STT and echo)

Download a model from <https://alphacephei.com/vosk/models> and unzip it into a `model/` folder next to the script.

The examples default to the larger US English model:

```
vosk-model-en-us-0.22   (~1.8 GB, more accurate)
```

You can also use the small model (`vosk-model-small-en-us-0.15`, ~50 MB) if you change the `model_path` in the source.

After unzipping, the folder layout should look like:

```
python-stt-tts-wireless/
├── wireless_livestttts_stt_tts.py
└── model/
    └── vosk-model-en-us-0.22/
        ├── am/
        ├── conf/
        └── ...
```

> The `model/` directory is git-ignored — model files are large and are not committed.

## Usage

```bash
# Speak a sentence out loud
python wireless_livestttts_stt_tts.py tts

# Listen and transcribe live from the microphone (Ctrl+C to stop)
python wireless_livestttts_stt_tts.py stt

# Listen, transcribe, and speak it back in a loop (say "stop it", "exit now", or "goodbye" to quit)
python wireless_livestttts_stt_tts.py echo
```

Running with no argument (or an unrecognized one) prints the usage message.

## How it works

### Text-to-Speech ([`text_to_speech()`](wireless_livestttts_stt_tts.py#L32))

Uses `pyttsx3` to synthesize speech locally. You can tune:

- **rate** — speaking speed in words per minute (default `175`)
- **volume** — `0.0` to `1.0` (default `1.0`)
- **voice** — pick a different installed voice (commented example in the code)

To **save to a WAV file** instead of speaking aloud, use `engine.save_to_file(text, "output.wav")` (see the commented snippet in the source).

### Speech-to-Text ([`speech_to_text()`](wireless_livestttts_stt_tts.py#L54))

Uses Vosk with a 16 kHz mono audio stream captured via `sounddevice`:

- Audio is captured in a background callback and pushed onto a queue.
- `KaldiRecognizer` consumes the audio and emits:
  - **partial** results (words recognized so far, printed inline with `...`)
  - **full** phrase results (printed as `You said: ...`)
- Press **Ctrl+C** to stop listening.

If the Vosk model can't be found at the given path, the script exits with a hint pointing to the model download page.

### Echo ([`echo()`](wireless_livestttts_stt_tts.py#L101))

Combines STT and TTS into a conversational loop: it listens, transcribes a phrase, and speaks it back, then prompts you for the next one.

- **TTS backend** — prefers the macOS `say` command (reliable for repeated calls) and falls back to `pyttsx3` on other platforms. Reusing `pyttsx3` across many `runAndWait()` calls can go silent after the first utterance on macOS, hence the preference for `say`.
- **Mic muting** — the input stream is paused while speaking so the program doesn't transcribe its own voice, and the audio queue is cleared afterward.
- **Noise handling** — a fresh `KaldiRecognizer` is created each turn, a short settle delay discards speaker echo, and a leading filler word Vosk tends to hallucinate from silence (e.g. `"the"`) is stripped.
- **Stopping** — say `"stop it"`, `"exit now"`, or `"goodbye"` to end the loop (it says "Goodbye" and exits).

## Project structure

```
python-stt-tts-wireless/
├── wireless_livestttts_stt_tts.py   # TTS + STT + echo examples with a small CLI
├── requirements.txt        # Python dependencies
├── .gitignore              # ignores model/, __pycache__/, venvs, etc.
├── model/                  # Vosk model(s) — git-ignored, downloaded separately
└── README.md
```

## Troubleshooting

- **`Could not load Vosk model ...`** — Make sure you downloaded and unzipped a Vosk model, and that its folder name matches the `model_path` (default `./model/vosk-model-en-us-0.22`).
- **No audio / PortAudio errors (Linux)** — Install `libportaudio2` (see above) and confirm your microphone is detected.
- **No voice / silent TTS (Linux)** — Install `espeak`.
- **Echo goes silent after the first reply (macOS)** — This is the `pyttsx3` reuse issue; echo mode uses the `say` command instead when it's on your `PATH`.
