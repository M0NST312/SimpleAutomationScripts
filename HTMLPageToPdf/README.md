# HTML Page to PDF Converter

Node.js scripts using Playwright to convert HTML pages to PDF documents.

## Purpose

These scripts launch a headless browser, navigate to a specified URL, and generate a PDF of the rendered page.

## Scripts

- `PDF.js`: Basic PDF generation
- `Scraper.js`: Advanced version with authentication and better error handling

## Requirements

- Node.js
- Playwright: `npm install playwright`

## Usage

### Basic Usage (PDF.js)

1. Edit the URL in `PDF.js`:
   ```javascript
   generatePDF("https://example.com");
   ```

2. Run the script:
   ```bash
   node PDF.js
   ```

3. The PDF will be saved as `output.pdf`

### Advanced Usage (Scraper.js)

1. Edit the URL and credentials in `Scraper.js`:
   ```javascript
   const url = "https://example.com";
   // And set httpCredentials if needed
   ```

2. Run the script:
   ```bash
   node Scraper.js
   ```

## Features

- Waits for page load and network idle
- Includes background graphics in PDF
- A4 format with margins
- Authentication support (in Scraper.js)
- Error handling and timeouts

## Configuration

You can modify:
- URL to convert
- Output filename
- PDF format and margins
- Authentication credentials
- Browser launch options (headless mode)

## Browser Profile

The `profile/` folder contains browser data that may be used for persistent sessions or cached data.