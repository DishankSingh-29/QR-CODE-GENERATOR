import qrcode
from PIL import Image

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

# ===================== Phase 1: Function to Generate QR Code =====================
def generate_qr_code(n):
    
    # ===================== Phase 2: Creating the QR Code Object =====================
    qr = qrcode.QRCode(
        version=1,  # Defines the QR code size (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction (up to 30% damage recovery)
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # White border around the QR code
    )
    
    # ===================== Phase 3: Collecting Data Based on User Choice =====================
    if n == 1:
        # Website URL QR Code
        website = input(f"\n{BOLD}{CYAN}Enter your Website URL: {END}")
        qr.add_data(website)
    
    elif n == 2:
        # vCard QR Code (Visiting Card)
        name = input(f"\n{BOLD}{CYAN}Enter your Name: {END}")
        phone = input(f"{BOLD}{CYAN}Enter your Phone Number: {END}")
        email = input(f"{BOLD}{CYAN}Enter your Email: {END}")
        company = input(f"{BOLD}{CYAN}Enter your Company Name: {END}")
        qr_data = f"BEGIN:VCARD\nFN:{name}\nTEL:{phone}\nEMAIL:{email}\nORG:{company}\nEND:VCARD"
        qr.add_data(qr_data)
    
    elif n == 3:
        # Geolocation QR Code
        lat = input(f"\n{BOLD}{CYAN}Enter Latitude: {END}")
        lon = input(f"{BOLD}{CYAN}Enter Longitude: {END}")
        qr.add_data(f"https://www.google.com/maps?q={lat},{lon}")
    
    elif n == 4:
        # Phone Number QR Code (Call)
        phone = input(f"\n{BOLD}{CYAN}Enter Phone Number: {END}")
        qr.add_data(f"tel:{phone}")
    
    elif n == 5:
        # Social Media QR Code
        social_link = input(f"\n{BOLD}{CYAN}Enter your Social Media Link: {END}")
        qr.add_data(social_link)
    
    elif n == 6:
        # PDF QR Code
        pdf_link = input(f"\n{BOLD}{CYAN}Enter PDF File Link: {END}")
        qr.add_data(pdf_link)
    
    else:
        print(f"\n{BOLD}{RED}Invalid option! Please choose a valid number.{END}")
        return

    qr.make(fit=True)  # Optimizes QR code size

    # ===================== Phase 4: Generating and Customizing the QR Code =====================
    fill_color = input(f"\n{BOLD}{PURPLE}Enter QR code color (or press Enter for default black): {END}").strip() or "black"
    back_color = input(f"{BOLD}{PURPLE}Enter background color (or press Enter for default white): {END}").strip() or "white"

    qr_img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # ===================== Phase 5: Saving and Displaying the QR Code =====================
    file_name = f"qr_code_{n}.png"  # Unique filename based on user selection
    qr_img.save(file_name)  # Saves the QR code as an image file
    qr_img.show()  # Opens the generated QR code image
    print(f"\n{RED}QR Code saved as {file_name}.{END}")  # Confirmation message

# ===================== Phase 6: User Interaction & Menu Selection =====================
option = int(input(f"""\n{UNDERLINE}{BOLD}{RED}
Select the option whose QR CODE you want to generate:{END}{CYAN}
(1) Website
(2) Visiting Card
(3) Geolocation (GPS Coordinates)
(4) Phone Number
(5) Social Media
(6) PDF{END}
{GREEN}{BOLD}
Enter your choice (1-6): """))
print(END)


generate_qr_code(option)  # Call the function with the user's choice