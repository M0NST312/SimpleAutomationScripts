import csv
import re

# --- Configuration ---
INPUT_FILE = "emails.csv"          # Input CSV file name
VALID_OUTPUT_FILE = "valid_emails.csv"
INVALID_OUTPUT_FILE = "invalid_emails.csv"
EMAIL_COLUMN = "email"             # Column name containing emails

# --- Email validation regex ---
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def is_valid_email(email):
    """Return True if email address is valid."""
    return bool(EMAIL_REGEX.match(email.strip()))

def main():
    valid_emails = []
    invalid_emails = []

    # Read input CSV file
    with open(INPUT_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        if EMAIL_COLUMN not in reader.fieldnames:
            raise ValueError(f"'{EMAIL_COLUMN}' column not found in CSV headers: {reader.fieldnames}")

        for row in reader:
            email = row[EMAIL_COLUMN].strip()
            if is_valid_email(email):
                valid_emails.append({"email": email})
            else:
                invalid_emails.append({"email": email})

    # Write valid emails
    with open(VALID_OUTPUT_FILE, "w", newline='', encoding='utf-8') as valid_file:
        writer = csv.DictWriter(valid_file, fieldnames=["email"])
        writer.writeheader()
        writer.writerows(valid_emails)

    # Write invalid emails
    with open(INVALID_OUTPUT_FILE, "w", newline='', encoding='utf-8') as invalid_file:
        writer = csv.DictWriter(invalid_file, fieldnames=["email"])
        writer.writeheader()
        writer.writerows(invalid_emails)

    print(f"✅ Valid emails saved to: {VALID_OUTPUT_FILE} ({len(valid_emails)} found)")
    print(f"❌ Invalid emails saved to: {INVALID_OUTPUT_FILE} ({len(invalid_emails)} found)")

if __name__ == "__main__":
    main()
