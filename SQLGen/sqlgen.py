import csv

def generate_insert_sql_from_csv(table_name, csv_file_path):
    """
    Generates an SQL INSERT statement from a CSV file using its headers as columns.

    :param table_name: Name of the SQL table
    :param csv_file_path: Path to the CSV file
    :return: SQL INSERT statement as a string
    """
    values_list = []

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        # Read the first row as column headers
        columns = next(reader)
        for row in reader:
            # Escape single quotes in strings
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
            values_list.append(f"({', '.join(row_escaped)})")

    values_str = ",\n  ".join(values_list)
    columns_str = ", ".join(columns)
    sql = f"INSERT INTO {table_name} ({columns_str})\nVALUES\n  {values_str};"
    return sql


def export_sql_to_file(sql, output_file_path):
    """
    Exports the SQL statement to a file.

    :param sql: The SQL string to write
    :param output_file_path: File path to save the SQL
    """
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(sql)
    print(f"SQL successfully saved to {output_file_path}")

# Example usage
if __name__ == "__main__":
    table_name = "CRMCompany"
    csv_file_path = "data.csv"  # Replace with your CSV file path
    output_file_path = "insert.sql" 

    sql_insert = generate_insert_sql_from_csv(table_name, csv_file_path)
    export_sql_to_file(sql_insert, output_file_path)
    #print(sql_insert)
