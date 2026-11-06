
import re
from rank_bm25 import BM25Okapi


def tokenize(text):
    """
    Convert text into lowercase word tokens.
    Keeps words, numbers, and contractions.
    """
    return re.findall(r"\b[\w']+\b", text.lower())


class BM25Retriever:
    def __init__(self, chunks):
        if not chunks:
            raise ValueError("Cannot initialize BM25 with empty chunks.")

        self.chunks = chunks

        # Tokenize every chunk's text
        self.tokenized_corpus = [
            tokenize(chunk["text"])
            for chunk in chunks
        ]

        # Build BM25 index
        self.bm25 = BM25Okapi(self.tokenized_corpus)

    def retrieve(self, query, top_k=5):
        """
        Return the top-k most relevant chunks.
        Each result includes metadata and its BM25 score.
        """
        query_tokens = tokenize(query)

        if not query_tokens:
            return []

        scores = self.bm25.get_scores(query_tokens)

        # Sort chunk indices by descending BM25 score
        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )

        results = []

        for rank, idx in enumerate(ranked_indices[:top_k], start=1):
            chunk = self.chunks[idx]

            results.append({
                **chunk,
                "score": float(scores[idx]),
                "rank": rank
            })

        return results
