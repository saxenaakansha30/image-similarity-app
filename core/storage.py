# Saves uploaded images safely.

import os
import uuid
from PIL import Image
from core import config

# Function to save the uploaded image
def save_uploaded_image(uploaded_file):
    _, ext = os.path.splitext(uploaded_file.name)
    
    unique_filename = f"{str(uuid.uuid4())}{ext}"
    image_path = os.path.join(config.IMAGE_DIR, unique_filename)

    with open(image_path, "wb") as buffer:
        buffer.write(uploaded_file.read())

    return image_path
