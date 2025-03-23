import json
import pandas as pd
import os

def load_data(json_path, image_folder="dataset/images"):
    """
    Loads a COCO-style dataset from JSON and converts it to a DataFrame.
    
    Args:
        json_path (str): Path to the COCO JSON file.
        image_folder (str): Path to the image directory.

    Returns:
        pd.DataFrame: DataFrame with "text" and "image" columns.
    """
    try:
        with open(json_path, "r") as f:
            coco_data = json.load(f)

        # Extract Image ID to Filename mapping
        image_id_to_filename = {img["id"]: os.path.join(image_folder, img["file_name"]) for img in coco_data["images"]}

        # Extract text annotations & match with images
        data = []
        for ann in coco_data["annotations"]:
            image_path = image_id_to_filename.get(ann["image_id"], None)
            caption = ann["caption"]
            if image_path:  # Ensure image exists
                data.append({"text": caption, "image": image_path})

        return pd.DataFrame(data)

    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return pd.DataFrame()  # Return empty DataFrame in case of failure
