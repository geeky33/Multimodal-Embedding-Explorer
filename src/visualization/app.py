import streamlit as st
import plotly.express as px
import pandas as pd
import torch
from sklearn.decomposition import PCA
from src.data_loader import load_data
from src.embedding_generator import EmbeddingGenerator

# 🔹 Streamlit App Title
st.title("📊 Multimodal Embedding Explorer")

# 🔹 Load Dataset (COCO JSON)
DATASET_PATH = "dataset/coco_subset.json"
IMAGE_FOLDER = "dataset/images"

st.sidebar.subheader("Dataset Info")
st.sidebar.write(f"📂 Using dataset: `{DATASET_PATH}`")

# Load Data
try:
    data = load_data(DATASET_PATH, IMAGE_FOLDER)
    if data.empty:
        st.error("⚠️ Dataset is empty! Check the file content.")
        st.stop()
except Exception as e:
    st.error(f"❌ Error loading dataset: {e}")
    st.stop()

# 🔹 Embedding Generator
embed_gen = EmbeddingGenerator()

# 🔹 Select Embedding Type
embedding_type = st.sidebar.radio("Choose Embedding Type:", ["Text", "Image"])

# 🔹 Generate Embeddings
st.sidebar.write("🔄 Generating embeddings...")

try:
    if embedding_type == "Text":
        embeddings = embed_gen.generate_embeddings(data["text"], None)[0]
    else:
        embeddings = embed_gen.generate_embeddings(None, data["image"])[1]

    # Convert to NumPy
    if isinstance(embeddings, torch.Tensor):
        embeddings = embeddings.detach().cpu().numpy()

    # Reduce Dimensions with PCA
    pca = PCA(n_components=3)
    reduced_embeddings = pca.fit_transform(embeddings)

    # 🔹 Create DataFrame for Visualization
    vis_df = pd.DataFrame(reduced_embeddings, columns=["x", "y", "z"])
    vis_df["text"] = data["text"]  # Add text for hover info

    # 🔹 Plot 3D Scatter Plot
    st.subheader("📌 3D Visualization of Embeddings")
    fig = px.scatter_3d(vis_df, x="x", y="y", z="z", hover_data=["text"])
    st.plotly_chart(fig)

except Exception as e:
    st.error(f"❌ Error generating embeddings: {e}")
