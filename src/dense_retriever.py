
import numpy as np
from sentence_transformers import SentenceTransformer


EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


class DenseRetriever:
    def __init__(self, chunks, embeddings_path="embeddings.npy"):
        if not chunks:
            raise ValueError("Cannot initialize with empty chunks.")

        self.chunks = chunks
        self.model = SentenceTransformer(EMBED_MODEL)

        # Load precomputed document embeddings
        self.embeddings = np.load(embeddings_path)

        # Validate that embeddings match the chunks
        if len(self.chunks) != len(self.embeddings):
            raise ValueError(
                f"Mismatch: {len(self.chunks)} chunks but "
                f"{len(self.embeddings)} embeddings."
            )

        if self.embeddings.ndim != 2:
            raise ValueError("Embeddings must be a 2D array.")

    def retrieve(self, query, top_k=5):
        """
        Retrieve chunks using cosine similarity.
        Returns metadata, similarity score, and rank.
        """
        if not query.strip():
            return []

        # Embed the query using the same model
        query_embedding = self.model.encode(
            [query],
            normalize_embeddings=True
        ).astype("float32")[0]

        # Normalized vectors: dot product = cosine similarity
        scores = self.embeddings @ query_embedding

        ranked_indices = np.argsort(scores)[::-1][:top_k]

        results = []

        for rank, idx in enumerate(ranked_indices, start=1):
            chunk = self.chunks[int(idx)]

            results.append({
                **chunk,
                "score": float(scores[idx]),
                "rank": rank
            })

        return results
