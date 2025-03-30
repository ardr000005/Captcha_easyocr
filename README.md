# CAPTCHA OCR Reader

## Overview
This is a Streamlit-based web application that utilizes EasyOCR to extract text from CAPTCHA images. The application allows users to upload CAPTCHA images, crop them if necessary, and extract text using optical character recognition (OCR).

## Features
- Upload CAPTCHA images in PNG, JPG, or JPEG format.
- Crop the image before processing.
- Apply preprocessing techniques like contrast enhancement and noise reduction.
- Use EasyOCR for accurate text extraction.

## Technologies Used
- Python
- Streamlit
- EasyOCR
- OpenCV
- NumPy
- Pillow (PIL)
- Streamlit Cropper

## Installation

### Prerequisites
Make sure you have Python 3.7 or later installed.

### Install Dependencies
Run the following command to install all required dependencies:
```sh
pip install streamlit easyocr numpy opencv-python pillow streamlit-cropper
```

## Usage

### Running the Application
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/captcha-ocr-reader.git
   cd captcha-ocr-reader
   ```

2. Run the Streamlit app:
   ```sh
   streamlit run captcha.py
   ```

### Uploading and Extracting Text
1. Upload a CAPTCHA image.
2. Crop the image if necessary.
3. Click "OK" to extract text.
4. View the extracted text in the application.

## File Structure
```
📁 captcha-ocr-reader
│-- 📄 captcha.py           # Main Streamlit application
│-- 📄 README.md        # Documentation
│-- 📄 requirements.txt # Dependencies
```

## Notes
- If OCR accuracy is low, consider tuning the parameters in `extract_text()` function.
- Ensure that `easyocr` is properly installed and supports your language.

## License
This project is licensed under the MIT License.

