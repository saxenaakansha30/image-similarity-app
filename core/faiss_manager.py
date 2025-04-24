# Integration with FAISS

import faiss
import numpy as np
import os
import pickle
from core import config

embedding_dim = 512 # Clip ViT-B/32 outputs 512 dimensional vectors
index_file = config.FIASS_INDEX_FILE
paths_file = config.IMAGE_PATH_FILE

if os.path.exists(index_file):
    index = faiss.read_index(index_file)
else:
    index = faiss.IndexFlatL2(embedding_dim) # create empty index using L2 distance (Euclidean)

if os.path.exists(paths_file):
    with open(paths_file, "rb") as file:
        image_paths = pickle.load(file)
else:
    image_paths = []

# Function to save the index and image paths to current state.
def save_index():
    faiss.write_index(index, index_file)
    with open(paths_file, "wb") as file:
        pickle.dump(image_paths, file)

# Function to add image embedding to the index
def add_to_index(embedding, image_path):
    global image_paths
    index.add(embedding)
    image_paths.append(image_path)
    save_index()

# Function to search for similar images
def search_similar(embedding, k=3):
    distance, indices = index.search(embedding, k)
    similar_images = [image_paths[i] for i in indices[0]]

    return similar_images