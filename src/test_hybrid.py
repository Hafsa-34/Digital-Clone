
import json

from bm25_retriever import BM25Retriever
from dense_retriever import DenseRetriever
from hybrid_retriever import HybridRetriever

# Load chunks
with open("chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

# Initialize both retrievers
bm25 = BM25Retriever(chunks)

dense = DenseRetriever(
    chunks,
    embeddings_path="embeddings.npy"
)

# Initialize hybrid retriever
hybrid = HybridRetriever(bm25, dense)

# Test query
query = "What are my cybersecurity career goals?"

results = hybrid.retrieve(
    query,
    top_k=5,
    candidate_k=10
)

print(f"\nQuery: {query}")
print("\nHybrid Retrieval Results:")

for result in results:
    print("\n------------------------------")
    print("Rank:", result["rank"])
    print("Chunk ID:", result["chunk_id"])
    print("Source:", result["source"])
    print("Section:", result["section"])
    print("RRF Score:", round(result["rrf_score"], 6))
    print("BM25 Rank:", result["bm25_rank"])
    print("Dense Rank:", result["dense_rank"])
    print("Text:", result["text"][:300], "...")
