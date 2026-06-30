import streamlit as st
import pandas as pd

from ranker import rank_candidates
from features import extract_keywords


# =====================================================
# Page Config
# =====================================================

st.set_page_config(
    page_title="Hybrid AI Candidate Ranking System",
    page_icon="🤖",
    layout="wide"
)


# =====================================================
# Header
# =====================================================

st.title("🤖 Hybrid AI Candidate Ranking System")

st.caption(
    "Feature Engineering + Semantic Search using Sentence Transformers (BAAI/bge-small-en-v1.5)"
)

st.markdown("""
This system ranks candidates using a **Hybrid AI Pipeline** that combines:

- 🔍 Feature Engineering
- 🧠 Semantic Search
- ⚡ Hybrid Ranking
- 📈 Explainable AI
""")


# =====================================================
# Job Description
# =====================================================

jd = st.text_area(
    "📄 Paste Job Description",
    height=250
)


# =====================================================
# Rank Button
# =====================================================

if st.button("🚀 Rank Candidates", use_container_width=True):

    if not jd.strip():
        st.warning("Please paste a Job Description.")
        st.stop()

    # -----------------------------------------------
    # Extract Keywords
    # -----------------------------------------------

    keywords = extract_keywords(jd)

    st.success("✅ Job Description analyzed successfully!")

    st.subheader("📌 Detected Skills")

    cols = st.columns(4)

    for i, skill in enumerate(keywords):
        cols[i % 4].success(skill.title())

    st.divider()

    # -----------------------------------------------
    # Dashboard
    # -----------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📂 Candidates",
        "100,000"
    )

    col2.metric(
        "🏆 Output",
        "Top 100"
    )

    col3.metric(
        "🤖 Model",
        "BGE Small"
    )

    col4.metric(
        "⚡ Ranking",
        "Hybrid AI"
    )

    st.divider()

    # -----------------------------------------------
    # Pipeline
    # -----------------------------------------------

    st.subheader("🔄 Ranking Pipeline")

    st.info("""
Job Description
→ Keyword Extraction
→ Feature Engineering
→ Top 300 Retrieval
→ Semantic Re-ranking
→ Top 100 Candidates
""")

    st.divider()

    # -----------------------------------------------
    # Ranking
    # -----------------------------------------------

    with st.spinner("Ranking 100,000 candidates..."):

        results = rank_candidates(jd)

    st.success("✅ Ranking Completed!")

    st.divider()

    # -----------------------------------------------
    # Candidate Results
    # -----------------------------------------------

    st.header("🏆 Top Candidates")

    export = []

    for rank, candidate in enumerate(results, start=1):

        with st.expander(f"🏅 Rank #{rank} | {candidate['headline']}"):

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Final Score",
                round(candidate["score"], 2)
            )

            c2.metric(
                "Semantic Match",
                f"{candidate['semantic_score']:.1f}%"
            )

            c3.metric(
                "Feature Score",
                candidate["feature_score"]
            )

            st.write(
                f"**Candidate ID:** `{candidate['candidate_id']}`"
            )

            st.write("### 💡 Why this candidate matched")

            st.info(candidate["reasoning"])

        export.append({

            "candidate_id": candidate["candidate_id"],
            "rank": rank,
            "score": candidate["score"],
            "reasoning": candidate["reasoning"]

        })

    st.divider()

    # -----------------------------------------------
    # Leaderboard
    # -----------------------------------------------

    st.subheader("📊 Leaderboard")

    df = pd.DataFrame(export)

    st.dataframe(
        df,
        use_container_width=True
    )

    st.download_button(

        "📥 Download Top 100 CSV",

        df.to_csv(index=False),

        "submission.csv",

        "text/csv",

        use_container_width=True

    )

    st.divider()

    # -----------------------------------------------
    # Architecture
    # -----------------------------------------------

    st.subheader("🏗️ System Architecture")

    st.code("""

            Job Description
                   │
                   ▼
         Keyword Extraction
                   │
                   ▼
         Feature Engineering
                   │
                   ▼
        Top 300 Candidate Retrieval
                   │
                   ▼
     Sentence Transformer (BGE)
                   │
                   ▼
          Cosine Similarity
                   │
                   ▼
          Hybrid AI Ranking
                   │
                   ▼
      Top 100 Ranked Candidates

""")

    st.divider()

    st.caption(
        "Built for the Redrob India Data & AI Challenge | Python • Streamlit • Sentence Transformers • Hybrid AI Ranking"
    )