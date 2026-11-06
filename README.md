---
title: Hafsa Digital Clone
emoji: 🪞
colorFrom: indigo
colorTo: purple
sdk: gradio
sdk_version: 5.34.2
python_version: 3.13
app_file: app.py
pinned: false
---
# Digital Clone (Hybrid RAG): AI clone, not the real person

Gradio app: BM25 + dense (all-MiniLM-L6-v2) retrieval, Reciprocal Rank Fusion, LLM answers in first person from retrieved chunks only. The API token is stored as the Space secret `HF_TOKEN`.

## Report

**1. Knowledge base and why.** [files, chunk counts, why chosen, rare keywords]

**2. Test questions**

| Question | BM25 result | Dense result | Hybrid result | Best mode and why |
|---|---|---|---|---|
| Q1 (exact rare keyword) | | | | |
| Q2 (paraphrase, no shared words) | | | | |
| Q3 | | | | |
| Q4 | | | | |
| Q5 | | | | |

**3. Failure case.** [question, answer given, correct answer, why it failed]

**4. Improvement.** [one concrete change]

Fusion used: Reciprocal Rank Fusion, score = sum of 1/(60 + rank). The alternative, weighted min-max fusion alpha*dense + (1-alpha)*bm25, is [one-sentence trade-off].