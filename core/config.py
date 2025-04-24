# Constants and Paths

import os

TOP_K = 3
IMAGE_DIR = "images"
INDEX_DIR = "faiss_index"

FIASS_INDEX_FILE = os.path.join(INDEX_DIR, "index_file.index")
IMAGE_PATH_FILE = os.path.join(INDEX_DIR, "image_paths.pkl")

os.makedirs(INDEX_DIR, exist_ok=True)
os.makedirs(INDEX_DIR, exist_ok=True)