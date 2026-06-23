# Python Barcode Generator & Reader

A small command-line toolkit that **generates** barcodes in many common
symbologies (Code128, Code39, EAN-13, EAN-8, UPC-A, ISBN-13, and more) and
**reads** them back from image files, printing the decoded data to the console.

- **Generator** — [`barcode_generator.py`](barcode_generator.py), built on
  [`python-barcode`](https://github.com/WhyNotHugo/python-barcode) +
  [Pillow](https://python-pillow.org/). Saves PNGs into [`resources/`](resources/).
- **Reader** — [`barcode_reader.py`](barcode_reader.py), built on
  [`pyzbar`](https://github.com/NaturalHistoryMuseum/pyzbar) (a wrapper around
  the native `zbar` library) + Pillow.

## Features

- Generate a barcode from any string with a single command.
- Choose from **21 barcode symbologies** (see [Supported barcode types](#supported-barcode-types)).
- Custom output file names.
- Built-in `--demo` mode that produces one sample of each common type.
- All images are written to the `resources/` directory automatically.

## Project structure

```
python-barcode-reader/
├── barcode_generator.py   # Generator script (CLI + reusable functions)
├── barcode_reader.py      # Reader/decoder script (CLI + reusable functions)
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── resources/             # Generated barcode PNGs are saved here
    ├── demo_code128.png
    ├── demo_code39.png
    ├── demo_ean13.png
    ├── demo_ean8.png
    ├── demo_upca.png
    ├── demo_isbn13.png
    └── code128_Hello_12345.png
```

## Requirements

- Python 3.7+
- Dependencies listed in [`requirements.txt`](requirements.txt):
  - `python-barcode` — barcode generation
  - `pillow` — image export / loading
  - `pyzbar` — barcode decoding (reading)
- **Native library for reading:** `pyzbar` needs the `zbar` shared library:
  - macOS: `brew install zbar`
  - Debian/Ubuntu: `sudo apt-get install libzbar0`
  - Windows: bundled with the `pyzbar` wheel (no extra step)

> On Apple-Silicon macOS the Homebrew `zbar` library lives in
> `/opt/homebrew/lib`, which Python does not search by default. The reader
> handles this automatically — no `DYLD_LIBRARY_PATH` configuration needed.

## Installation

```bash
# (optional) create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate

# install Python dependencies
pip install -r requirements.txt

# install the native zbar library (needed by the reader)
brew install zbar                # macOS
# sudo apt-get install libzbar0  # Debian/Ubuntu
```

## Usage — generating barcodes

The script is invoked as `python barcode_generator.py [data] [options]`.

### Generate a basic barcode (defaults to Code128)

```bash
python barcode_generator.py "Hello-12345"
# -> resources/code128_Hello_12345.png
```

### Generate a specific barcode type

```bash
python barcode_generator.py 5901234123457 --type ean13
# -> resources/ean13_5901234123457.png
```

### Use a custom output file name

```bash
python barcode_generator.py 5901234123457 --type ean13 --name my_product
# -> resources/my_product.png
```

### Generate one sample of every common type (demo)

```bash
python barcode_generator.py --demo
```

### List all supported barcode types

```bash
python barcode_generator.py --list
```

## Usage — reading barcodes

Decode barcodes from images with
`python barcode_reader.py [image ...]` and print the results to the console.

### Read a single image

```bash
python barcode_reader.py resources/demo_ean13.png
# resources/demo_ean13.png: [EAN13] 5901234123457
#
# Decoded 1 barcode(s) from 1 image(s).
```

### Read multiple images

```bash
python barcode_reader.py resources/demo_ean13.png resources/demo_code128.png
```

### Read every PNG in resources/ (no arguments)

```bash
python barcode_reader.py
# resources/code128_Hello_12345.png: [CODE128] Hello-12345
# resources/demo_code128.png:        [CODE128] CODE128-DEMO-001
# resources/demo_ean13.png:          [EAN13] 5901234123457
# ...
#
# Decoded 7 barcode(s) from 7 image(s).
```

The output format is `<image path>: [<TYPE>] <decoded data>`, one line per
barcode found. Images with no detectable barcode print `no barcode detected`.
The process exits non-zero if nothing could be decoded.

## Command-line options

### Generator (`barcode_generator.py`)

| Option            | Short | Description                                                        |
| ----------------- | ----- | ------------------------------------------------------------------ |
| `data`            |       | The data to encode (positional). Required unless `--demo`/`--list`.|
| `--type <type>`   | `-t`  | Barcode symbology to use. Default: `code128`.                      |
| `--name <name>`   | `-n`  | Output file name without extension. Default: `<type>_<data>`.      |
| `--demo`          | `-d`  | Generate one sample barcode per common type.                       |
| `--list`          | `-l`  | List all supported barcode types and exit.                         |

### Reader (`barcode_reader.py`)

| Argument   | Description                                                             |
| ---------- | ----------------------------------------------------------------------- |
| `images`   | Image file(s) to decode. If omitted, reads every PNG in `resources/`.   |

## Supported barcode types

`codabar`, `code128`, `code39`, `ean`, `ean13`, `ean13-guard`, `ean14`,
`ean8`, `ean8-guard`, `gs1`, `gs1_128`, `gtin`, `isbn`, `isbn10`, `isbn13`,
`issn`, `itf`, `jan`, `nw-7`, `pzn`, `upc`, `upca`

Run `python barcode_generator.py --list` to print the current list from your
installed version.

## Input rules per symbology

Some symbologies validate the input length and/or compute a checksum digit, so
the payload must be numeric and of a specific length:

| Type      | Input requirement                              | Example          |
| --------- | ---------------------------------------------- | ---------------- |
| `code128` | Any ASCII text                                 | `Hello-12345`    |
| `code39`  | Uppercase letters, digits and a few symbols    | `CODE39DEMO`     |
| `ean13`   | 12 digits (13th is an auto-computed checksum)  | `590123412345`   |
| `ean8`    | 7 digits (8th is an auto-computed checksum)    | `9638507`        |
| `upca`    | 11 digits (12th is an auto-computed checksum)  | `03600029145`    |
| `isbn13`  | 13-digit ISBN starting with 978/979            | `9781492056355`  |

If you pass invalid data the script prints a clear error message and exits with
a non-zero status code.

## Using it as a library

Both scripts can also be imported and used from other Python code:

```python
from barcode_generator import generate, supported_types
from barcode_reader import read_barcodes

# generate() returns the absolute path of the written PNG
path = generate("5901234123457", code_type="ean13", name="my_product")
print("Saved:", path)
print("Available types:", supported_types())

# read_barcodes() returns a list of {"type": ..., "data": ...} dicts
for item in read_barcodes(path):
    print(item["type"], item["data"])   # EAN13 5901234123457
```

## Output

All generated images are saved to the [`resources/`](resources/) directory as
`.png` files. The directory is created automatically if it does not exist.

## License

Provided as-is for demonstration / proof-of-concept purposes.


### working logs 
```
adarshkumar@adarshs-MacBook-Pro-16-new python-barcode-reader % python3 barcode_generator.py "adarsh-kumar"
Barcode saved to: /Volumes/WORK/poc/python-barcode-reader/resources/code128_adarsh_kumar.png
adarshkumar@adarshs-MacBook-Pro-16-new python-barcode-reader % python3  barcode_reader.py ./resources/code128_adarsh_kumar.png
./resources/code128_adarsh_kumar.png: [CODE128] adarsh-kumar

Decoded 1 barcode(s) from 1 image(s).
```
