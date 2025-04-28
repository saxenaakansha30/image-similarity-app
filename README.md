# Image Similarity Tool (using CLIP + FAISS)

This is a small project where I built a simple image similarity search tool using two open-source libraries: **CLIP** (by OpenAI) and **FAISS** (by Meta).

You can:

- Upload images to build an index
- Search for similar images by uploading a new image
- Or search by entering a text query

The app is built with **Streamlit** for quick testing and demo purposes.

---

# How to Run

1. **Clone the repository**

```bash
git clone https://github.com/saxenaakansha30/image-similarity-app.git
cd image-similarity-app
```

2. **Set up the virtual environment**

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
# or
.\venv\Scripts\activate      # Windows
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

4. **Start the Streamlit app**

```bash
streamlit run streamlit_ui/app.py
```

---

# 🛠️ Tech Stack

- [CLIP](https://github.com/openai/CLIP) (OpenAI)
- [FAISS](https://github.com/facebookresearch/faiss) (Meta)
- Streamlit
- Python

---

# Related Blog Post

Learn more about this project and the challenges I faced here:  
[Image Similarity Tool – Blog Post](https://akanshasaxena.com/post/image-similarity-tool/)

---

# Acknowledgements

- OpenAI for CLIP
- Meta for FAISS
- The open-source community for making these amazing tools available!

