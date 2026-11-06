
import json
from bm25_retriever import BM25Retriever

# Load existing chunks
with open("chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

# Initialize retriever
retriever = BM25Retriever(chunks)

# Test query
query = "What are my cybersecurity career goals?"

results = retriever.retrieve(query, top_k=3)

print(f"\nQuery: {query}")
print("\nBM25 Results:")

for result in results:
    print("\n------------------------------")
    print("Rank:", result["rank"])
    print("Chunk ID:", result["chunk_id"])
    print("Source:", result["source"])
    print("Section:", result["section"])
    print("Score:", round(result["score"], 4))
    print("Text:", result["text"][:300], "...")
