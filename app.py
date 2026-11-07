
import json
import os
import re
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

# Load local .env file
ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")

# Load Streamlit Cloud secret when deployed
try:
    if not os.getenv("GROQ_API_KEY"):
        if "GROQ_API_KEY" in st.secrets:
            os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
except Exception:
    pass

# Import our existing project components
from src.bm25_retriever import BM25Retriever
from src.dense_retriever import DenseRetriever
from src.hybrid_retriever import HybridRetriever
from src.generator import DigitalCloneGenerator

# Visual theme (CSS, animated mascot, hero) lives in theme.py
from theme import CSS, STREAMLIT_CSS, FOOTER, hero_html


def _flat(html: str) -> str:
    """Collapse whitespace so Streamlit's markdown parser keeps the HTML block intact."""
    return re.sub(r">\s+<", "><", re.sub(r"\s*\n\s*", " ", html)).strip()


# ---------- Page configuration ----------

st.set_page_config(
    page_title="Hafsa's Digital Clone",
    page_icon="🤖",
    layout="wide"
)

st.markdown(_flat(f"<style>{CSS}{STREAMLIT_CSS}</style>"), unsafe_allow_html=True)

# Themed header: animated mascot + the required "AI clone" banner
st.markdown(_flat(hero_html()), unsafe_allow_html=True)

st.write(
    "Ask questions about Hafsa. "
    "Answers are generated using her personal knowledge base."
)


# ---------- Load project components ----------

@st.cache_resource
def load_components():

    with open(ROOT / "chunks.json", encoding="utf-8") as file:
        chunks = json.load(file)

    bm25 = BM25Retriever(chunks)

    dense = DenseRetriever(
        chunks,
        embeddings_path=str(ROOT / "embeddings.npy")
    )

    hybrid = HybridRetriever(bm25, dense)

    generator = DigitalCloneGenerator()

    return chunks, bm25, dense, hybrid, generator


try:
    chunks, bm25, dense, hybrid, generator = load_components()

except Exception as error:
    st.error(f"Could not initialize the application: {error}")
    st.stop()


# ---------- Sidebar ----------

st.sidebar.header("Settings")

mode = st.sidebar.selectbox(
    "Choose retrieval mode",
    ["BM25 only", "Dense only", "Hybrid"],
    index=2
)

top_k = st.sidebar.slider(
    "Number of retrieved chunks",
    min_value=1,
    max_value=6,
    value=4
)

st.sidebar.divider()

st.sidebar.caption(
    "Knowledge base: 9 personal documents"
)

st.sidebar.caption(
    f"Available chunks: {len(chunks)}"
)


# ---------- Question input ----------

with st.form("question_form"):

    question = st.text_area(
        "Your question",
        placeholder="What are my long-term career goals?",
        height=100
    )

    submitted = st.form_submit_button(
        "Ask",
        type="primary",
        use_container_width=True
    )


# ---------- Retrieval and generation ----------

if submitted:

    if not question.strip():
        st.warning("Please enter a question.")

    else:

        try:

            with st.spinner("Retrieving relevant information..."):

                if mode == "BM25 only":
                    retrieved = bm25.retrieve(
                        question,
                        top_k=top_k
                    )

                elif mode == "Dense only":
                    retrieved = dense.retrieve(
                        question,
                        top_k=top_k
                    )

                else:
                    retrieved = hybrid.retrieve(
                        question,
                        top_k=top_k
                    )

            with st.spinner("Generating your answer..."):

                answer = generator.generate(
                    question,
                    retrieved
                )

            st.subheader("Generated Answer")
            st.markdown(
                f'<div class="bubble">\n\n{answer}\n\n</div>',
                unsafe_allow_html=True
            )

            st.divider()

            st.subheader("Retrieved Chunks")

            st.caption(
                f"Mode: {mode} | "
                f"Retrieved passages: {len(retrieved)}"
            )

            if not retrieved:
                st.info("No relevant chunks were retrieved.")

            for index, hit in enumerate(retrieved, start=1):

                score = hit.get(
                    "score",
                    hit.get("rrf_score", 0.0)
                )

                with st.expander(
                    f"#{index} | {hit['source']} | "
                    f"Score: {score:.4f}"
                ):

                    st.write(
                        f"**Chunk ID:** {hit['chunk_id']}"
                    )

                    st.write(
                        f"**Source:** {hit['source']}"
                    )

                    st.write(
                        f"**Retrieval score:** {score:.6f}"
                    )

                    if "bm25_rank" in hit:
                        st.write(
                            f"**BM25 rank:** {hit['bm25_rank']}"
                        )

                    if "dense_rank" in hit:
                        st.write(
                            f"**Dense rank:** {hit['dense_rank']}"
                        )

                    st.markdown("**Retrieved passage:**")
                    st.write(hit["text"])

        except Exception as error:
            st.error(
                f"An error occurred while processing your question: {error}"
            )


# ---------- Footer ----------

st.divider()

st.caption(
    "Digital Clone | Hybrid Retrieval-Augmented Generation "
    "(BM25 + Dense + Reciprocal Rank Fusion)"
)

st.markdown(_flat(FOOTER), unsafe_allow_html=True)