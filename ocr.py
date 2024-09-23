import easyocr
reader = easyocr.Reader(['en', 'hi'])  # English and Hindi languages
extracted_text = reader.readtext('uploaded_image.png', detail=0)
