# Constants and Paths

import os

IMAGE_DIR = "images"
INDEX_DIR = "faiss_index"

FIASS_INDEX_FILE = os.path.join(INDEX_DIR, "index_file.index")
IMAGE_PATH_FILE = os.path.join(INDEX_DIR, "image_paths.pkl")

os.mkdir(INDEX_DIR, exist_ok=True)
os.mkdir(INDEX_DIR, exist_ok=True)