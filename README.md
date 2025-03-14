# QR Code Generator

## Overview
This is a custom QR Code Generator that allows users to generate QR codes for various types of data, including website URLs, vCards, geolocation coordinates, phone numbers, social media links, and PDF files. Users can also customize the QR code colors.

## Features
- Generate QR codes for different data types:
  - Website URLs
  - Visiting Cards (vCard format)
  - Geolocation (GPS Coordinates)
  - Phone Numbers
  - Social Media Links
  - PDF File Links
- Customize QR code colors (foreground and background).
- Save and display generated QR codes automatically.
- High error correction level (up to 30% damage recovery).

## Installation

### Prerequisites
Ensure you have the following installed on your system:
- Python 3+
- Required dependencies: `qrcode` and `PIL` (Pillow)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/qr-code-generator.git
   cd qr-code-generator
   ```
2. Install dependencies:
   ```sh
   pip install qrcode[pil]
   ```

## Usage

### Running the QR Code Generator
Run the script in the terminal:
```sh
python qr_generator.py
```

### User Options
Upon execution, the program prompts the user to choose a QR code type from the following options:
1. Website URL
2. Visiting Card (vCard)
3. Geolocation (GPS Coordinates)
4. Phone Number
5. Social Media Link
6. PDF File Link

The user then provides the necessary details, selects colors, and the QR code is generated, displayed, and saved.

## Example
Generating a QR code for a website:
```sh
Enter your choice (1-6): 1
Enter your Website URL: https://example.com
Enter QR code color (or press Enter for default black): blue
Enter background color (or press Enter for default white): yellow
QR Code saved as qr_code_1.png.
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-new-option`).
3. Commit your changes.
4. Push to your branch and create a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any issues or suggestions, feel free to open an issue or reach out at `dishanksingh36@gmail.com`.
