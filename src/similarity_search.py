import faiss
import numpy as np

class SimilaritySearch:
    def __init__(self, embeddings):
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)

    def search(self, query_embedding, k=5):
        distances, indices = self.index.search(query_embedding, k)
        return distances, indices
