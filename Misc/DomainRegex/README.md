# Domain Regex Generator

A Python script to generate email validation regex patterns from a list of domains.

## Purpose

This script reads a CSV file containing domain names and generates a regex pattern that can be used to validate email addresses belonging to those domains.

## Requirements

- Python 3.x

## Input Format

Create a `domains.csv` file with a "domain" column:

```csv
domain
example.com
test.org
company.net
```

## Usage

1. Create `domains.csv` with your domain list.

2. Run the script:
   ```bash
   python domains.py
   ```

3. The script will generate a regex pattern and save it to `results.txt` as JSON.

## Output

The generated regex follows the pattern: `^[^@]+@(<escaped_domains>)$`

For example, with domains `example.com` and `test.org`:
```
^[^@]+@(example\.com|test\.org)$
```

This regex matches any email where the domain is in your list.

## Features

- Automatically escapes dots in domain names
- Outputs JSON format for easy parsing
- Handles CSV with proper encoding
- Simple and dependency-free