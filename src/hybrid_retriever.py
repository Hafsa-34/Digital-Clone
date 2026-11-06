
class HybridRetriever:
    def __init__(self, bm25_retriever, dense_retriever, rrf_k=60):
        self.bm25 = bm25_retriever
        self.dense = dense_retriever
        self.rrf_k = rrf_k

    def retrieve(self, query, top_k=5, candidate_k=10):
        """
        Combine BM25 and dense rankings using
        Reciprocal Rank Fusion.
        """

        bm25_results = self.bm25.retrieve(
            query, top_k=candidate_k
        )

        dense_results = self.dense.retrieve(
            query, top_k=candidate_k
        )

        combined = {}

        # Add BM25 rankings
        for result in bm25_results:
            chunk_id = result["chunk_id"]

            combined[chunk_id] = {
                **result,
                "rrf_score": 1 / (
                    self.rrf_k + result["rank"]
                ),
                "bm25_rank": result["rank"],
                "dense_rank": None,
                "bm25_score": result["score"],
                "dense_score": None
            }

        # Add dense rankings
        for result in dense_results:
            chunk_id = result["chunk_id"]

            dense_contribution = 1 / (
                self.rrf_k + result["rank"]
            )

            if chunk_id in combined:
                combined[chunk_id]["rrf_score"] += dense_contribution
                combined[chunk_id]["dense_rank"] = result["rank"]
                combined[chunk_id]["dense_score"] = result["score"]
            else:
                combined[chunk_id] = {
                    **result,
                    "rrf_score": dense_contribution,
                    "bm25_rank": None,
                    "dense_rank": result["rank"],
                    "bm25_score": None,
                    "dense_score": result["score"]
                }

        # Sort by combined RRF score
        ranked_results = sorted(
            combined.values(),
            key=lambda x: x["rrf_score"],
            reverse=True
        )

        results = []

        for rank, result in enumerate(
            ranked_results[:top_k], start=1
        ):
            result["rank"] = rank
            results.append(result)

        return results
