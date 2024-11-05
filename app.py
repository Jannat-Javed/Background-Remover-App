import streamlit as st
from rembg import remove
from PIL import Image
import io

# Set up page configuration
st.set_page_config(page_title="Background Remover", layout="centered")

# Add a header image or banner
st.title("Background Remover App")
st.write("Remove backgrounds from your images effortlessly. Upload an image, and get a transparent background version in seconds!")

# Add styling with custom CSS
st.markdown("""
    <style>
    .stButton>button {
        color: white;
        background-color: #4CAF50;
        border-radius: 8px;
        padding: 0.5em 1em;
        margin-top: 10px;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# File uploader for users to upload images
uploaded_file = st.file_uploader("Upload an image (png, jpg, jpeg, webp)", type=["png", "jpg", "jpeg", "webp"])

# Layout for image processing
if uploaded_file is not None:
    col1, col2 = st.columns(2)

    # Display the original image
    with col1:
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_column_width=True)

    # Remove background from the image
    with st.spinner("Removing background... Please wait!"):
        output_image = remove(original_image)

    # Display the image with background removed
    with col2:
        st.image(output_image, caption="Background Removed", use_column_width=True)

    # Prepare image for download
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Add a download button
    st.download_button(
        label="Download Image with Background Removed",
        data=byte_im,
        file_name="background_removed.png",
        mime="image/png",
        key='download-btn'
    )
else:
    st.info("Please upload an image to get started.")
