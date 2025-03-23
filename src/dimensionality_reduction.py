from sklearn.decomposition import PCA

def reduce_dimensions(embeddings, n_components=3):
    pca = PCA(n_components=n_components)
    reduced_embeddings = pca.fit_transform(embeddings)
    return reduced_embeddings
