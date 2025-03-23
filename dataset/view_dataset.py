import streamlit as st
import json
import os
import base64
from PIL import Image
from io import BytesIO

# Define the dataset file path
DATASET_PATH = "outputs/dataset/coco_subset.json"

def base64_to_image(base64_string):
    """Convert a base64 string to a PIL Image."""
    image_data = base64.b64decode(base64_string)
    return Image.open(BytesIO(image_data))

def load_dataset():
    """Load dataset from JSON file."""
    if not os.path.exists(DATASET_PATH):
        st.error(f"Dataset file not found: {DATASET_PATH}")
        return []

    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# Streamlit UI
st.title("📊 Facebook PMD Dataset Viewer")
st.write(f"Showing dataset from `{DATASET_PATH}`")

# Load dataset
dataset = load_dataset()

# Display dataset
if dataset:
    for i, sample in enumerate(dataset):
        st.subheader(f"Sample {i+1}")
        
        # Show image
        if "image" in sample:
            image = base64_to_image(sample["image"])
            st.image(image, caption=f"Sample {i+1} Image", use_column_width=True)
        
        # Show text data
        for key, value in sample.items():
            if key != "image":
                st.write(f"**{key}:** {value}")

        st.markdown("---")  # Separator
else:
    st.warning("No data found in the dataset.")

