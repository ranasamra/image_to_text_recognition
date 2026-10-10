import streamlit as st
import pytesseract
from PIL import Image
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if necessary)

st.set_page_config(page_title="Image Text Extractor", page_icon="🔍", layout="wide")

st.title("🔍 Image / Text Recognition")
st.write("Upload an image to extract text from it using Optical Character Recognition (OCR).")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.subheader("Uploaded Image")
    st.image(image, caption='Uploaded Image', use_container_width=True)

    image_array = np.array(image)

    gray_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)

    processed_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    text = pytesseract.image_to_string(processed_image)

    st.subheader("Recognized Text")
    if text.strip():
        st.text_area("Extracted Text", value=text, height=200)
    else:
        st.warning("No text could be extracted from the image.")