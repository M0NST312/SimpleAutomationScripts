import base64
import os

def encode_file_to_base64(file_path):
    """
    Reads a file and returns its Base64-encoded string.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No such file: {file_path}")

    with open(file_path, "rb") as file:
        encoded_bytes = base64.b64encode(file.read())
        encoded_str = encoded_bytes.decode("utf-8")

    return encoded_str


if __name__ == "__main__":
    # Ask user for file path
    file_path = input("Enter the path to your file: ").strip()

    try:
        # Encode file
        base64_string = encode_file_to_base64(file_path)

        # Create output path
        output_path = file_path + ".b64.txt"

        # Save Base64 to output file
        with open(output_path, "w", encoding="utf-8") as out_file:
            out_file.write(base64_string)

        print("\n✅ Base64 encoding successful!")
        print(f"💾 Encoded file saved to: {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")
