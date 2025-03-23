import streamlit as st
import pandas as pd

def annotation_interface(data):
    st.title('Annotation Interface')
    for index, row in data.iterrows():
        st.image(row['image_path'])
        annotation = st.text_input(f"Annotation for {row['image_path']}", key=index)
        data.at[index, 'annotation'] = annotation
    return data
