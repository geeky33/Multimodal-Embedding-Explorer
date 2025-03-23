import plotly.express as px
import pandas as pd

def plot_embeddings(embeddings, labels):
    df = pd.DataFrame(embeddings, columns=['x', 'y', 'z'])
    df['label'] = labels
    fig = px.scatter_3d(df, x='x', y='y', z='z', color='label', hover_data=['label'])
    fig.show()
