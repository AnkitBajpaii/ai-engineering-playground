##
## Concept    : Text Embeddings & Cosine Similarity (OpenAI Embeddings API)
## What it does: Generates vector embeddings for pairs of words/phrases using OpenAI's
##               text-embedding-3-small model, then computes cosine similarity to measure
##               how semantically related each pair is.
## What you'll learn:
##   - What embeddings are: fixed-size numerical vectors that represent the meaning of text
##   - How to call client.embeddings.create() and extract the embedding vectors
##   - How cosine similarity works: a score of 1.0 = identical meaning, 0.0 = unrelated
##   - Why "mango shake" and "mango" score higher similarity than "phone" and "car"
##   - The foundation for semantic search, clustering, and recommendation systems
## Run: python 6.embedding_sample.py
##
from openai import OpenAI
from dotenv import load_dotenv
import numpy as np

load_dotenv()

client = OpenAI()

inputs = [
    ["mango shake", "mango"],
    ["ice cream", "vanilla"],
    ["phone", "car"],
]

for _input in inputs:

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=_input
        )

    embedding_a = response.data[0].embedding
    embedding_b = response.data[1].embedding

    cosine_similarity = np.dot(embedding_a, embedding_b) / (np.linalg.norm(embedding_a) * np.linalg.norm(embedding_b))

    print(f"Cosine similarity between '{_input[0]}' and '{_input[1]}': {cosine_similarity}\n")