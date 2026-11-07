# Digital Clone – Hafsa Sarfraz

**Live App:** https://hafsasarfraz-digital-clone.streamlit.app/

## 1. Knowledge Base and Selection

I selected nine personal Markdown documents covering my biography, education, skills and experience, hobbies and interests, opinions, daily routine, goals, FAQs, and projects/research. I chose these documents because they contain the personal information, experiences, interests, and career goals that my Digital Clone should be able to answer questions about.

The documents were divided into 25 chunks of approximately 200–300 words, with 40 words of overlap. Each chunk retains its source filename and chunk ID.

## 2. Retrieval Evaluation

I evaluated five questions using BM25, Dense, and Hybrid retrieval. The system uses `rank_bm25` for keyword retrieval, `all-MiniLM-L6-v2` with cosine similarity for dense retrieval, and Reciprocal Rank Fusion (RRF) to combine rankings.

| Question | BM25 result | Dense result | Hybrid result | Best mode and why |
|---|---|---|---|---|
| **Q1.** What are my favourite songs? | 04-Hobbies&Interests::000, Retrieval score: 7.793853 | 08-FAQs::002, Retrieval score: 0.445918 | 04-Hobbies&Interests::000, Retrieval score: 7.793853 | **BM25** — retrieves 04-Hobbies&Interests::000, which directly matches the exact keywords and personal-interest information. |
| **Q2.** Which compositions do I most often put on during my downtime? *(Paraphrase)* | 02-Education::000, Retrieval score: 6.327306 | 08-FAQs::002, Retrieval score: 0.385957 | 06-DailyRoutine&StudyHabits::001, Retrieval score: 5.966099 | **Dense** — retrieves 08-FAQs::002, suggesting it understands the semantic meaning of the paraphrased question better than BM25's keyword matching. Verify that this chunk actually contains the favourite songs before finalizing. |
| **Q3.** What are my cybersecurity career goals? | 08-FAQs::001, 4.218354 | 07-Goals&FuturePlans::000, Retrieval score: 0.677018 | 07-Goals&FuturePlans::000, Retrieval score: 4.157685 | **Hybrid** — ranks 07-Goals&FuturePlans::000 first, providing the more detailed career-goal information while benefiting from both keyword and semantic retrieval. |
| **Q4.** What is SentinelEdge? *(Rare exact keyword)* | 09-Projects&Research::000, Retrieval score: 4.577828 | 09-Projects&Research::000, Retrieval score: 0.416721 | 09-Projects&Research::000, Retrieval score: 4.577828 | **Hybrid (tie with BM25 and Dense)** — all three methods retrieve 09-Projects&Research::000. This indicates that the exact rare keyword makes the relevant project chunk easy to retrieve across all methods. |
| **Q5.** What is my favourite car brand? *(Information absent from knowledge base)* | I don't have that in my notes. | I don't have that in my notes. | I don't have that in my notes. | **All three (tie)** — all methods correctly handle missing information by returning the required fallback: "I don't have that in my notes." No method has a clear advantage. |

## 3. Failure Case

In the cybersecurity career-goals test, BM25 ranked `08-FAQs::001` above the more detailed `07-Goals&FuturePlans::000` chunk. Although the FAQ contains relevant information, it is a weaker first retrieval when more detailed career-goal information is needed. This happened because BM25 relies on keyword matching and can rank a short FAQ highly when it contains matching terms.

## 4. Proposed Improvement

One improvement would be to introduce a reranking stage that evaluates the relevance of the retrieved chunks before passing them to the LLM. Although all three retrieval methods successfully retrieved the SentinelEdge project chunk and correctly handled the unknown car-brand question, their results differed for other questions. For example, BM25 retrieved the most relevant hobbies chunk for the favourite-songs question, while Dense retrieval was selected for the paraphrased music question. A reranking stage could help prioritize the most informative passages and improve retrieval consistency across different types of questions.

## 5. Conclusion

The test results demonstrate that no single retrieval method performs best for every question. BM25 performed best for exact keyword-based retrieval, Dense retrieval was more suitable for the paraphrased music question, and Hybrid retrieval provided the strongest result for the cybersecurity career-goals question. All three methods successfully retrieved the SentinelEdge project information and returned the expected fallback for information absent from the knowledge base. Overall, combining keyword-based and semantic retrieval through Reciprocal Rank Fusion provides a flexible approach for the Digital Clone, while allowing users to compare retrieved passages and generated answers.

**Deployment:** Streamlit Community Cloud  
**LLM:** Groq – `openai/gpt-oss-20b`  
**Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2`  
**Hybrid Fusion:** Reciprocal Rank Fusion (RRF)
