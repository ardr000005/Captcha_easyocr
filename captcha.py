import streamlit as st
import numpy as np
import cv2
from PIL import Image
import io
from streamlit_cropper import st_cropper
import easyocr

# Initialize EasyOCR Reader
reader = easyocr.Reader(['en'])

# Streamlit UI
st.title("CAPTCHA OCR Reader")

# File Uploader
uploaded_file = st.file_uploader("Upload CAPTCHA Image", type=["png", "jpg", "jpeg"])

def preprocess_image(image):
    image_np = np.array(image.convert("RGB"))
    gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)

    # Increase contrast
    alpha = 1.5  # Contrast control
    beta = 10    # Brightness control
    contrast_img = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)

    # Apply Gaussian Blur to reduce noise
    blur = cv2.GaussianBlur(contrast_img, (3, 3), 0)
    
    return blur

def extract_text(image):
    try:
        processed_image = preprocess_image(image)
        result = reader.readtext(processed_image, detail=0, low_text=0.3, text_threshold=0.7)
        return "".join(result) if result else "Error: No text detected"
    except Exception as e:
        return f"Error: {e}"

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded CAPTCHA", use_column_width=True)
    
    # Crop Image
    st.write("Crop the image if necessary:")
    cropped_image = st_cropper(image, box_color="blue")
    
    if cropped_image is not None:
        cropped_pil = cropped_image.convert("RGB")
        if st.button("OK"):  # User confirmation before processing
            text_result = extract_text(cropped_pil)
            st.write("Extracted Text:", text_result)
    else:
        st.write("Using original image for OCR.")
        if st.button("OK"):
            text_result = extract_text(image)
            st.write("Extracted Text:", text_result)
