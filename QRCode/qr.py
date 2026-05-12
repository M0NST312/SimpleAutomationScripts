import os
import sys

try:
    import qrcode
    from PIL import Image
    #print(f"Using qrcode version: {qrcode.__version__}")
except ImportError as e:
    print(f"Import error: {e}")
    print("Please install the required packages:")
    print("pip install qrcode[pil]")
    sys.exit(1)
except AttributeError as e:
    print(f"Attribute error: {e}")
    print("There might be a naming conflict. Check if you have a file named 'qrcode.py' in your directory.")
    sys.exit(1)

def generate_qr_code(data, filename="qrcode.png", size=10, border=4):
    """
    Generate a QR code from the given data
    
    Args:
        data (str): The data to encode in the QR code
        filename (str): Output filename (default: "qrcode.png")
        size (int): Size of each box in pixels (default: 10)
        border (int): Border size in boxes (default: 4)
    """
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=size,  # Size of each box in pixels
        border=border,  # Border size in boxes
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save(filename)
    print(f"QR code saved as: {filename}")
    
    return img

def main():
    # Get input from user
    data = input("Enter the text/URL to encode in QR code: ")
    filename = input("Enter filename (press Enter for 'qrcode.png'): ").strip()
    
    if not filename:
        filename = "qrcode.png"
    
    # Generate QR code
    try:
        generate_qr_code(data, filename)
        print("QR code generated successfully!")
        
        # Ask if user wants to open the image
        open_img = input("Do you want to open the image? (y/n): ").lower()
        if open_img == 'y':
            if os.name == 'nt':  # Windows
                os.startfile(filename)
            elif os.name == 'posix':  # macOS and Linux
                os.system(f'open {filename}')  # macOS
                # For Linux, you might need: os.system(f'xdg-open {filename}')
                
    except Exception as e:
        print(f"Error generating QR code: {e}")

if __name__ == "__main__":
    main()