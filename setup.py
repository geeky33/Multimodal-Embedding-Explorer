from setuptools import setup, find_packages

setup(
    name='multimodal_embedding_explorer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'plotly',
        'pandas',
        'numpy',
        'scikit-learn',
        'transformers',
        'torch',
    ],
)