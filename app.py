import streamlit as st
import easyocr
from PIL import Image
import numpy as np
import torch

st.title("OCR App (Hindi & English)")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Open the image using PIL
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image')

    # Convert the PIL image to a numpy array
    image_np = np.array(image)

    # Run OCR
    reader = easyocr.Reader(['en', 'hi'])
    result = reader.readtext(image_np, detail=0)
    
    # Display extracted text
    extracted_text = " ".join(result)
    st.write("Extracted Text:", extracted_text)

    # Search functionality: Enter keywords to search within the extracted text
    search_query = st.text_input("Enter keyword to search")
    
    if search_query:
        # Highlight the matching keyword within the text
        if search_query.lower() in extracted_text.lower():
            st.write(f"Keyword '{search_query}' found!")
            # Highlight the keyword in the extracted text
            highlighted_text = extracted_text.replace(
                search_query, f"**{search_query}**"
            )
            st.markdown(highlighted_text)
        else:
            st.write(f"Keyword '{search_query}' not found.")
