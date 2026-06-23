# Python QR Code Reader

Decode QR codes from an image file or a live webcam stream. Uses OpenCV's
built-in `QRCodeDetector`, so there's no native `zbar` system dependency to install.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

Read from an image file:

```bash
python qr_reader.py image path/to/qr.png
python3  qr_reader.py image ./resources/adarsh.png
python3  qr_reader.py image ./resources/john.png
python3  qr_reader.py image ./resources/marry.png
python3  qr_reader.py image ./resources/walter.png
```

Output as JSON (includes bounding-box corner points):

```bash
python qr_reader.py image path/to/qr.png --json
```

Read from a webcam (press `q` or `Esc` to quit):

```bash
python qr_reader.py webcam
python qr_reader.py webcam --camera 1   # pick a non-default camera
```

## Exit codes

| Code | Meaning                          |
|------|----------------------------------|
| 0    | At least one QR code decoded     |
| 1    | Error (file not found, no camera)|
| 2    | Ran fine, but no QR code found   |

## Generating QR codes from the console

`qr_generator.py` reads the data to encode from the console and writes the
QR code image (PNG) into the `resources/` directory, which is created
automatically.

### Interactive mode

Run with no arguments and the script prompts for the data and a file name:

```bash
python qr_generator.py
```

```text
Enter the text or URL to encode: https://github.com/adarsh
Enter the output file name (e.g. adarsh): adarsh
QR code saved to: /.../resources/adarsh.png
Encoded data:     'https://github.com/adarsh'
```

### Non-interactive mode

Pass the data and file name as arguments:

```bash
python qr_generator.py "https://github.com/adarsh" adarsh   # -> resources/adarsh.png
```

Then decode it with the reader:

```bash
python qr_reader.py image ./resources/adarsh.png
```

### Details

- **Output** — black-on-white PNG saved under `resources/`, auto-sized to fit
  the data, with error-correction level M (~15% recovery).
- **Safe file names** — the file name is sanitized: directory components are
  stripped, a trailing `.png` is removed, and unsafe characters become `_`,
  so console input can never write outside `resources/`. For example,
  `../../etc/key` is saved as `key.png`.
- **Validation** — empty data or file name is rejected.
- **Exit codes** — `0` on success, `1` on error (empty input or cancelled).
- **Tuning** — error correction, `box_size`, `border`, and colors can be
  adjusted in `generate_qr()`. See [WIKI.md](WIKI.md) for the full reference.


### work log 
```
(.venv) adarshkumar@adarshs-MacBook-Pro-16-new python-qrcode-reader % python qr_generator.py "https://github.com/radha" radha   
QR code saved to: /Volumes/WORK/GIT/python/APPLICATION/python-qrcode-reader/resources/radha.png
Encoded data:     'https://github.com/radha'
(.venv) adarshkumar@adarshs-MacBook-Pro-16-new python-qrcode-reader % python3  qr_reader.py image ./resources/radha.png 
[1] https://github.com/radha
(.venv) adarshkumar@adarshs-MacBook-Pro-16-new python-qrcode-reader % 
```