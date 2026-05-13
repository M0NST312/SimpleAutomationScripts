# QR Code Generator

A Python script to generate QR codes from text or URLs.

## Purpose

This script creates QR code images from user-provided text, URLs, or any data that can be encoded in a QR code.

## Requirements

- Python 3.x
- qrcode library: `pip install qrcode[pil]`
- PIL (Pillow): `pip install pillow`

## Usage

1. Run the script:
   ```bash
   python qr.py
   ```

2. Enter the text/URL to encode when prompted.

3. Optionally enter a filename (defaults to `qrcode.png`).

4. The QR code image will be generated and saved.

5. Optionally open the image automatically.

## Features

- Interactive input for data and filename
- Configurable QR code parameters (version, error correction, size, border)
- Automatic image opening on Windows/macOS/Linux
- Error handling for missing dependencies

## Customization

You can modify the `generate_qr_code` function parameters:
- `version`: QR code size (1 = smallest)
- `error_correction`: Error correction level (L, M, Q, H)
- `box_size`: Pixel size of each box
- `border`: Border thickness in boxes

## Output

- PNG image file containing the QR code
- Black QR code on white background
- Suitable for printing or digital use