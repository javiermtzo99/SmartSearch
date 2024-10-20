import faiss
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

def get_index_and_model(df:pd.DataFrame):
    # Load the SentenceTransformer model (auto-detects GPU if available)
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Generate embeddings for the discussion data
    embeddings = model.encode(df['discussion_text'].tolist(), batch_size=16, show_progress_bar=True)

    # Convert to numpy array
    embeddings = np.array(embeddings)

    # Define the dimension of embeddings
    d = embeddings.shape[1]

    # Create the FAISS index
    index = faiss.IndexFlatL2(d)  # L2 distance (Euclidean)

    index.add(embeddings)

    return model, index