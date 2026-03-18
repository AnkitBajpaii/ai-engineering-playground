##
## Concept    : Embedding Similarity Metrics — Euclidean Distance, Cosine Similarity & Dot Product
## What it does: Computes three different mathematical similarity/distance measures between
##               two fixed 3-dimensional vectors, demonstrating how each metric behaves.
## What you'll learn:
##   - Euclidean distance: straight-line distance between two points in vector space.
##     Lower = more similar. Sensitive to the magnitude (length) of the vectors.
##   - Cosine similarity: measures the angle between two vectors, not their magnitude.
##     Ranges from -1 to 1; higher = more similar. Most common metric for text embeddings.
##   - Dot product: related to cosine similarity but also influenced by vector magnitude.
##     Used in many neural network attention mechanisms.
##   - Why cosine similarity is preferred for text: two documents with the same words
##     but different lengths should still be "similar" — cosine handles this, euclidean doesn't.
## Note: This file uses fixed vectors (no API call) — great for understanding the math in isolation.
## Run: python 12.embedding_similarity.py
##
from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity
import numpy as np

#define two vectors
embedding1 = np.array([1.5, 2.0, 3.5])
embedding2 = np.array([4.0, 1.0, 2.5])

print(f"Embedding 1: {embedding1}")
print(f"Embedding 2: {embedding2}")

euclidean_distance = euclidean_distances([embedding1], [embedding2])[0][0]

print(f"Euclidean distance between the two embeddings: {euclidean_distance}")

# Calculate cosine similarity
cosine_sim = cosine_similarity([embedding1], [embedding2])[0][0]
print("Cosine similarity between the two embeddings:", cosine_sim)

# Calculate the dot product
dot_product = np.dot(embedding1, embedding2)
print("Dot product:", dot_product)