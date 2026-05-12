import csv
import re
import chardet

INPUT_FILE = "emails.csv"
VALID_OUTPUT_FILE = "valid_emails.csv"
INVALID_OUTPUT_FILE = "invalid_emails.csv"
EMAIL_COLUMN = "email"

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def is_valid_email(email):
    if not email or not email.strip():
        return False
    return bool(EMAIL_REGEX.match(email.strip()))

def main():
    # Detect encoding
    with open(INPUT_FILE, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        print(f"Detected encoding: {encoding}")

    valid_emails = []
    invalid_emails = []

    # Read using detected encoding
    with open(INPUT_FILE, newline='', encoding=encoding, errors='replace') as csvfile:
        reader = csv.DictReader(csvfile)
        if EMAIL_COLUMN not in reader.fieldnames:
            raise ValueError(f"'{EMAIL_COLUMN}' column not found in CSV headers: {reader.fieldnames}")

        for row in reader:
            email = row.get(EMAIL_COLUMN, "").strip()
            if is_valid_email(email):
                valid_emails.append({"email": email})
            else:
                invalid_emails.append({"email": email})

    with open(VALID_OUTPUT_FILE, "w", newline='', encoding='utf-8') as valid_file:
        writer = csv.DictWriter(valid_file, fieldnames=["email"])
        writer.writeheader()
        writer.writerows(valid_emails)

    with open(INVALID_OUTPUT_FILE, "w", newline='', encoding='utf-8') as invalid_file:
        writer = csv.DictWriter(invalid_file, fieldnames=["email"])
        writer.writeheader()
        writer.writerows(invalid_emails)

    print(f"✅ Valid emails saved to: {VALID_OUTPUT_FILE} ({len(valid_emails)} found)")
    print(f"❌ Invalid emails saved to: {INVALID_OUTPUT_FILE} ({len(invalid_emails)} found)")

if __name__ == "__main__":
    main()
