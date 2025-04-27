# Integration with CLIP model

import torch
import clip
from PIL import Image
from core import config

if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

model, preprocess = clip.load("ViT-B/32", device=device)

def get_image_embedding(image_path):
    pil_image = Image.open(image_path)
    processed_image = preprocess(pil_image) # Adds resize, crop, normalization (0, -1) range as per CLIP model needs.
    image_tensor = processed_image.unsqueeze(0) # Adds a batch dimension to make it 4 dimensional
    image_tensor = image_tensor.to(device) # Move image tensor to GPU or CPU 

    with torch.no_grad():
        embedding_tensor = model.encode_image(image_tensor) # returns 512 dimensional vector embedding
        # no_grad() saved memory and computations by stating that we dont need gradient calculations

    embedding_numpy = embedding_tensor.cpu().numpy() # Moves back to cpu and return numpy array

    return embedding_numpy

def get_text_embedding(text):
    text_tensor = clip.tokenize([text]).to(device) # Tokenizes the text and moves to GPU or CPU
    with torch.no_grad():
        embedding_tensor = model.encode_text(text_tensor)
    
    embedding_numpy = embedding_tensor.cpu().numpy() # Moves back to cpu and return numpy array

    return embedding_numpy