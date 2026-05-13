\# 🧩 CSV → SQL Insert Generator

Lightweight Python scripts that convert CSV data into SQL `INSERT` statements.

## Scripts

- `sqlgen.py`: Generates a single INSERT statement for small datasets
- `sqlgen_batch.py`: Generates batched INSERT statements for large datasets

## 🚀 Features

- ✅ Automatically detects CSV headers as table columns
- ✅ Converts each row into valid SQL `INSERT` statements
- ✅ Escapes single quotes (`O'Brien → O''Brien`)
- ✅ Converts empty cells to `NULL`
- ✅ Splits large CSVs into batches (default = 1000 rows per insert)
- ✅ Exports results to `.sql` or `.txt`
- ✅ Uses only Python's built-in libraries — **no dependencies**

## Requirements

- Python 3.x

## 🧠 Example

### Example CSV (`data.csv`)

```csv
id,name,email
1,Alice,alice@example.com
2,Bob,bob@example.com
3,Charlie,charlie@example.com
```

### Generated SQL (sqlgen.py)

```sql
INSERT INTO YourTable (id, name, email)
VALUES
  (1, 'Alice', 'alice@example.com'),
  (2, 'Bob', 'bob@example.com'),
  (3, 'Charlie', 'charlie@example.com');
```

### Batched SQL (sqlgen_batch.py)

For large datasets, creates multiple INSERT statements with up to 1000 rows each.

## Usage

### Single Insert

1. Edit `sqlgen.py`:
   ```python
   table_name = "YourTable"
   csv_file_path = "data.csv"
   output_file_path = "insert.sql"
   ```

2. Run:
   ```bash
   python sqlgen.py
   ```

### Batched Inserts

1. Edit `sqlgen_batch.py`:
   ```python
   table_name = "YourTable"
   csv_file_path = "data.csv"
   batch_size = 1000
   output_file_path = "inserts.sql"
   ```

2. Run:
   ```bash
   python sqlgen_batch.py
   ```

## Data Types

- **Numbers**: Preserved as-is
- **Strings**: Properly escaped
- **Empty values**: Converted to `NULL`



