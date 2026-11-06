"""Run ONCE from the project root:  python src/BuildIndex.py
Chunks data/ (Chunking.py), embeds the chunks, and saves chunks.json + embeddings.npy
in the project root, where app.py loads them. Commit both files to the Space."""
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from Chunking import ROOT, load_documents, build_chunks, report

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def main():
    docs = load_documents(ROOT / "data", check_placeholders=True)  # refuses DUMMY DATA / TODO / [ANSWER]
    chunks = build_chunks(docs)
    report(chunks)
    model = SentenceTransformer(EMBED_MODEL)
    emb = model.encode([c["text"] for c in chunks], normalize_embeddings=True,
                       show_progress_bar=True).astype("float32")
    np.save(ROOT / "embeddings.npy", emb)
    with open(ROOT / "chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=1)
    print("Saved embeddings.npy and chunks.json in", ROOT)

if __name__ == "__main__":
    main()