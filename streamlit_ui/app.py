import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.clip_utils import get_image_embedding
from core.faiss_manager import add_to_index, search_similar, reset_index
from core.storage import save_uploaded_image, remove_uploaded_image
from core import config 
from PIL import Image

st.set_page_config(page_title="Image Similarity Tool", layout="wide")
st.title("Image Similarity Tool")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Action selector
    action = st.radio("What do you want to do?", ("Add to Index", "Search Similar Images"))

    if st.button("Submit"):
        image_path = save_uploaded_image(uploaded_file)
        st.image(image_path, caption="Uploaded image", width=250) # Show uploaded image
        embedding = get_image_embedding(image_path)

        if action == "Add to Index":
            add_to_index(embedding, image_path)
            st.success("Image added to index successfully!")
        else:
            similar_images = search_similar(embedding, config.TOP_K)
            st.subheader(f"Top {config.TOP_K} Similar Images")
            
            for sim_path in similar_images:
                st.image(sim_path, width=200)

            remove_uploaded_image(image_path)

st.markdown("RESET INDEX")
if st.button("Reset Entire Index"):
    reset_index()
    st.warning("Index reset successfully!")
