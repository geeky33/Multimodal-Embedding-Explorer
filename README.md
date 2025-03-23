# Multimodal Embedding Explorer

This repository provides interactive visualization tools for exploring joint embeddings from multimodal models like CLIP, LLaVa, and GPT-4V using Datumaro and OTX.

## 📁 Repository Structure

```plaintext
Multimodal-Embedding-Explorer/
│── dataset/              # Sample dataset files
│── docs/                 # Documentation and guides
│── notebooks/            # Jupyter notebooks for experiments
│── outputs/              # Model-generated outputs
│── src/                  # Main source code
│   ├── visualization/    # Interactive visualization tools (Streamlit, Plotly)
│   ├── embeddings/       # Embedding computation scripts
│   ├── preprocessing/    # Data preprocessing scripts
│── tests/                # Unit tests
│── LICENSE               # License information
│── README.md             # Project description
│── requirements.txt      # Python dependencies
│── setup.py              # Installation script
```
 
An interactive visualization and annotation tool for exploring joint embedding spaces using open-source models like CLIP.  

## Features  
- Compute embeddings for images and text using CLIP.  
- Visualize embeddings in 3D space using Plotly.  
- Filter, zoom, and explore dataset relationships.  
- Annotate noisy/mislabeled data.  
- Perform fast similarity search with FAISS.  

## Installation  
```sh
git clone https://github.com/your-username/Multimodal-Embedding-Explorer.git
cd Multimodal-Embedding-Explorer
pip install -r requirements.txt
```

## Usage 
```python
src/visualization.py
```

