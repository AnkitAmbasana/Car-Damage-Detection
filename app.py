import streamlit as st
from model_helper import predict
from PIL import Image
import base64

st.title("Car Damage Detection")

uploaded_file = st.file_uploader("Upload the file", type=["jpg", "png"])

if uploaded_file:
    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Determine orientation
    img = Image.open(image_path)
    width, height = img.size
    is_landscape = width >= height

    # Encode image to base64 to embed in HTML
    buffered = open(image_path, "rb")
    img_bytes = buffered.read()
    encoded = base64.b64encode(img_bytes).decode()

    display_width = 500 if is_landscape else 300

    st.markdown(
        f"""
        <div style="text-align:center;">
            <img src="data:image/jpeg;base64,{encoded}" width="{display_width}" style="margin-bottom: 10px;" />
        </div>
        """,
        unsafe_allow_html=True
    )

    prediction = predict(image_path)
    st.info(f"Predicted Class: {prediction}")
