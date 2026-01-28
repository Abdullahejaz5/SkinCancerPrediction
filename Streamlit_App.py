# app.py
import streamlit as st
import cv2
import tempfile
from tensorflow.keras.models import load_model


st.title("Skin Cancer Diagnosis")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    # Load image using OpenCV
    img = cv2.imread(temp_file_path)

    if img is not None:
        img_resized = cv2.resize(img, (224, 224))
        img_preprocessed = img_resized / 255.0
        img_preprocessed = img_preprocessed.reshape(1, 224, 224, 3)

        model1 = load_model('final_model.keras')
        result=model1.predict(img_preprocessed)[0][0]

        if result>0.5:
            ans='Cancer Predicted (MALIGNANT)'
        else:
            ans='No Cancer Predicted (BENIGN)'

        st.write(ans)

    else:
        st.error("Error: Could not read the uploaded image.")

else:
    st.info("Please upload an image to proceed.")
