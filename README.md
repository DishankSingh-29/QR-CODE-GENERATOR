# QR Code Generator
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

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
   git clone https://github.com/DishankSingh-29/qr-code-generator.git
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
python QR_Code_Generator.py
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
| UserInput | QR Code |
|----------------|---------------|
| <img src="https://github.com/user-attachments/assets/fe653dd7-d9f0-45e3-9632-bcb1d192f9a9" alt="Screenshot 2025-03-16 205048" width="450">| <img src="https://github.com/user-attachments/assets/828acb00-8312-446b-a6c5-951d1a48ea65" alt="Screenshot 2025-03-16 205018" width="450"> |  


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
