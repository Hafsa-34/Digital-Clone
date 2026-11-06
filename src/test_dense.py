
import json
from dense_retriever import DenseRetriever

with open("chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

retriever = DenseRetriever(
    chunks,
    embeddings_path="embeddings.npy"
)

query = "What are my cybersecurity career goals?"
results = retriever.retrieve(query, top_k=3)

print(f"\nQuery: {query}")
print("\nDense Retrieval Results:")

for result in results:
    print("\n------------------------------")
    print("Rank:", result["rank"])
    print("Chunk ID:", result["chunk_id"])
    print("Source:", result["source"])
    print("Section:", result["section"])
    print("Cosine similarity:", round(result["score"], 4))
    print("Text:", result["text"][:300], "...")
