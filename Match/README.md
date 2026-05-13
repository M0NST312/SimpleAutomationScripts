# Excel Sheet Matcher

A Python script to match data between two Excel sheets and export results to CSV.

## Purpose

This script reads two sheets from an Excel file, matches rows based on specified columns, and exports the matched data to a CSV file.

## Requirements

- Python 3.x
- pandas: `pip install pandas`
- openpyxl: `pip install openpyxl` (for .xlsx files)

## Configuration

Edit the configuration variables at the bottom of `match.py`:

```python
EXCEL_FILE = "path/to/your/file.xlsx"
SHEET1_NAME = "Sheet1"
SHEET2_NAME = "Sheet2"
MATCH_COLUMN_SHEET1 = "ColumnName1"  # or column index
MATCH_COLUMN_SHEET2 = "ColumnName2"  # or column index
OUTPUT_CSV = "matched_results.csv"
```

## Usage

1. Update the configuration variables with your file paths and column names.

2. Run the script:
   ```bash
   python match.py
   ```

3. The script will:
   - Read both sheets
   - Convert match columns to strings and strip whitespace
   - Perform an inner join on the matching columns
   - Export results to CSV

## Output

- Console output shows the number of matched rows and column names
- `matched_results.csv` contains all matched data with suffixes for duplicate column names

## Features

- Handles large Excel files
- Automatic data type conversion for matching
- Detailed progress logging
- Error handling for missing files or invalid sheet/column names