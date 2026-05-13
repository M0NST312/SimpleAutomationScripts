# Email Cleaner and Validator

Python scripts to clean and validate email addresses from CSV files.

## Purpose

These scripts process a CSV file containing email addresses, validate them using regex, and separate valid and invalid emails into separate output files.

## Scripts

- `clean_email.py`: Basic version
- `clean_email_v2.py`: Improved version with encoding detection and error handling

## Requirements

- Python 3.x
- For v2: `chardet` library (`pip install chardet`)

## Input Format

The input CSV file should have a column named "email" containing the email addresses to validate.

Example `emails.csv`:
```csv
email
user@example.com
invalid-email
another@domain.org
```

## Usage

1. Place your `emails.csv` file in the same directory as the script.

2. Run the script:
   ```bash
   python clean_email_v2.py  # Recommended
   # or
   python clean_email.py
   ```

3. The script will create:
   - `valid_emails.csv`: Contains only valid email addresses
   - `invalid_emails.csv`: Contains invalid email addresses

## Validation Rules

Emails are validated using the regex pattern: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`

This checks for:
- Alphanumeric characters, dots, underscores, percent, plus, and hyphens in the local part
- @ symbol
- Valid domain format

## Output

The script displays the number of valid and invalid emails found, and the paths to the output files.

## Improvements in v2

- Automatic encoding detection for the input CSV
- Better error handling for malformed files
- Handles empty email fields