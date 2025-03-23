from datasets import load_dataset
import os
import json
import base64
from io import BytesIO
from PIL import Image

# Dataset details
DATASET_NAME = "facebook/pmd"
CONFIG_NAME = "coco"  # You can change this if needed
NUM_SAMPLES = 10  # Fetch only 10 samples
SAVE_PATH = "outputs/dataset"

def image_to_base64(image):
    """
    Converts a PIL Image to a base64-encoded string.
    """
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def download_and_save_dataset(dataset_name, config_name, save_path, num_samples):
    """
    Streams a dataset from Hugging Face, converts images to base64, and saves the first `num_samples` locally.
    """
    print(f"🚀 Running download_dataset.py ...")
    print(f"📥 Streaming dataset: {dataset_name} (Config: {config_name})...")

    # Load dataset with streaming
    dataset = load_dataset(dataset_name, config_name, split="train", streaming=True, trust_remote_code=True)

    # Create output directory
    os.makedirs(save_path, exist_ok=True)
    file_path = os.path.join(save_path, f"{config_name}_subset.json")

    # Fetch and process samples
    data_list = []
    for i, sample in enumerate(dataset):
        if i >= num_samples:
            break
        
        # Convert image to base64 if it exists
        if "image" in sample and isinstance(sample["image"], Image.Image):
            sample["image"] = image_to_base64(sample["image"])
        
        data_list.append(sample)
        print(f"✅ Fetched {i+1} samples...")

    # Save to JSON file
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data_list, f, indent=4)

    print(f"✅ Successfully saved {num_samples} samples to {file_path}")

if __name__ == "__main__":
    download_and_save_dataset(DATASET_NAME, CONFIG_NAME, SAVE_PATH, NUM_SAMPLES)
