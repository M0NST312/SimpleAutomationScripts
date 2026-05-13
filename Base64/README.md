# Base64 Encoder

A simple Python script to encode any file to Base64 format.

## Purpose

This script reads a file, encodes its contents to Base64, and saves the encoded string to a new file with a `.b64.txt` extension.

## Requirements

- Python 3.x

## Usage

1. Run the script:
   ```bash
   python encode_base64.py
   ```

2. When prompted, enter the path to the file you want to encode.

3. The script will create a new file with the same name plus `.b64.txt` extension containing the Base64-encoded data.

## Example

```
Enter the path to your file: example.pdf
✅ Base64 encoding successful!
💾 Encoded file saved to: example.pdf.b64.txt
```

## Features

- Handles any file type
- Uses UTF-8 encoding for the output text file
- Provides clear success/error messages