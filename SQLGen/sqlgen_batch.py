import csv
import math

def generate_insert_sql_from_csv(table_name, csv_file_path, batch_size=1000):
    """
    Generates batched SQL INSERT statements from a CSV file using its headers as columns.

    :param table_name: Name of the SQL table
    :param csv_file_path: Path to the CSV file
    :param batch_size: Maximum number of rows per INSERT
    :return: List of SQL INSERT statements (one per batch)
    """
    all_rows = []

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        columns = next(reader)  # Read header row
        for row in reader:
            row_escaped = []
            for value in row:
                # Treat empty strings as NULL
                if value == "":
                    row_escaped.append("NULL")
                # If numeric, leave as is
                elif value.replace('.', '', 1).isdigit():
                    row_escaped.append(value)
                else:
                    row_escaped.append(f"'{value.replace('\'', '\'\'')}'")
            all_rows.append(f"({', '.join(row_escaped)})")

    # Split rows into batches
    total_batches = math.ceil(len(all_rows) / batch_size)
    columns_str = ", ".join(columns)
    sql_batches = []

    for i in range(total_batches):
        start = i * batch_size
        end = start + batch_size
        batch_rows = all_rows[start:end]
        values_str = ",\n  ".join(batch_rows)
        sql = f"INSERT INTO {table_name} ({columns_str})\nVALUES\n  {values_str};"
        sql_batches.append(sql)

    return sql_batches


def export_sql_batches(sql_batches, output_file_path):
    """
    Writes multiple SQL statements to a file.

    :param sql_batches: List of SQL strings
    :param output_file_path: Path of output file
    """
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for i, sql in enumerate(sql_batches, start=1):
            file.write(f"-- Batch {i}\n")
            file.write(sql + "\n\n")
    print(f"✅ SQL successfully saved to {output_file_path} ({len(sql_batches)} batches written)")


# Example usage
if __name__ == "__main__":
    table_name = "[IHRMS].[dbo].[EmpInfo]"
    csv_file_path = "empin.csv"       # Replace with your CSV file path
    output_file_path = "default_insert.sql"  # Output file
    batch_size = 750               # Number of rows per SQL INSERT

    sql_batches = generate_insert_sql_from_csv(table_name, csv_file_path, batch_size)
    export_sql_batches(sql_batches, output_file_path)
