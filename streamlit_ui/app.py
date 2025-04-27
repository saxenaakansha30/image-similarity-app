import streamlit as st
import sys
import os
import logging

logging.getLogger("streamlit.watcher.local_sources_watcher").setLevel(logging.ERROR)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.clip_utils import get_image_embedding, get_text_embedding
from core.faiss_manager import add_to_index, search_similar, reset_index
from core.storage import save_uploaded_image, remove_uploaded_image
from core import config 
from PIL import Image

## HELPER FUNCTIONS
def handle_uploaded_image(uploaded_file):
    """
    Handle the uploaded image: saves, display and returns the image path.
    """
    if uploaded_file is not None:
        image_path = save_uploaded_image(uploaded_file)
        st.image(image_path, caption="Uploaded image", width=250) # Show uploaded image

        return image_path

    return None


## STREAMLIT UI

st.set_page_config(page_title="Image Similarity Tool", layout="wide")
st.title("Image Similarity Tool")

tab_add, tab_search, tab_reset = st.tabs(["Add Image to Index", "Search Similar Images", "Reset Index"])

with tab_add:
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key="add_image")

    if st.button("Add"):
        image_path = handle_uploaded_image(uploaded_file)
        if image_path is not None:
            embedding = get_image_embedding(image_path)
            add_to_index(embedding, image_path)
            st.success("Image added to index successfully!")

with tab_search:
    search_action = st.radio("How do you want to search?", ("None", "Search by Image", "Search by Text"))
    embedding = None

    if search_action == "Search by Image":
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key="search_image")
    
        if st.button("Search"):
            image_path = handle_uploaded_image(uploaded_file)

            if image_path is not None:
                embedding = get_image_embedding(image_path)
                remove_uploaded_image(image_path)
    elif search_action == "Search by Text":
        text_query = st.text_input("Enter text query:")
        if st.button("Search") and text_query:
            embedding = get_text_embedding(text_query)
    else:
        st.error("Please upload an image or enter text to search.")

    if embedding is not None:
        similar_images = search_similar(embedding, config.TOP_K)
        st.subheader(f"Top {config.TOP_K} Similar Images")

        if not similar_images:
            st.warning("No similar images found.")
        else:
            for sim_path in similar_images:
                st.image(sim_path, width=200)

with tab_reset:
    if st.button("Reset Entire Index"):
        reset_index()
        st.warning("Index reset successfully!")