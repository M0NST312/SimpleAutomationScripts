\# 🧩 CSV → SQL Insert Generator



A lightweight Python script that converts CSV data into SQL `INSERT` statements.  

It automatically reads column names from the CSV header, escapes text safely, handles `NULL` values, and splits the output into batches (default: 1,000 rows per statement) to avoid SQL size limits.



---



\## 🚀 Features



\- ✅ Automatically detects CSV headers as table columns  

\- ✅ Converts each row into valid SQL `INSERT` statements  

\- ✅ Escapes single quotes (`O'Brien → O''Brien`)  

\- ✅ Converts empty cells to `NULL`  

\- ✅ Splits large CSVs into batches (default = 1000 rows per insert)  

\- ✅ Exports results to `.sql` or `.txt`  

\- ✅ Uses only Python's built-in libraries — \*\*no dependencies\*\*



---



\## 🧠 Example



\### Example CSV (`data.csv`)



```csv

id,name,email

1,Alice,alice@example.com

2,Bob,bob@example.com

3,Charlie,charlie@example.com



