import streamlit as st
import pandas as pd

from ranker import rank_candidates
from features import extract_keywords


st.set_page_config(
    page_title="AI Recruiter",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Recruiter")
st.caption("Hybrid AI Candidate Ranking Engine")


st.markdown("""
Paste a Job Description below and discover the best matching AI candidates using

- Feature Engineering
- Semantic Search
- Hybrid Ranking
- Explainable AI
""")


jd = st.text_area(
    "Paste Job Description",
    height=250
)


if st.button("🔍 Find Candidates"):

    if not jd.strip():
        st.warning("Please paste a Job Description.")
        st.stop()

    keywords = extract_keywords(jd)

    st.success("Job Description Analyzed")

    st.subheader("📌 Detected Skills")

    cols = st.columns(4)

    for i, skill in enumerate(keywords):

        cols[i % 4].success(skill.title())

    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Candidates Scanned",
        "10,000"
    )

    col2.metric(
        "Retrieved",
        "300"
    )

    col3.metric(
        "Final Ranked",
        "100"
    )

    st.divider()

    with st.spinner("Ranking candidates..."):

        results = rank_candidates(jd)

    st.header("🏆 Top Candidates")

    export = []

    for rank, candidate in enumerate(results, start=1):

        with st.expander(
            f"#{rank} | {candidate['headline']}"
        ):

            c1, c2 = st.columns(2)

            c1.metric(
                "Final Score",
                round(candidate["score"], 2)
            )

            c2.metric(
                "Semantic Match",
                f"{candidate['semantic_score']:.1f}%"
            )

            st.write(
                f"**Candidate ID:** {candidate['candidate_id']}"
            )

            st.write(
                f"**Feature Score:** {candidate['feature_score']}"
            )

            st.write("### Why this candidate matched")

            st.info(candidate["reasoning"])

        export.append({

            "candidate_id":
                candidate["candidate_id"],

            "rank":
                rank,

            "score":
                candidate["score"],

            "reasoning":
                candidate["reasoning"]

        })

    st.divider()

    st.subheader("📊 Leaderboard")

    df = pd.DataFrame(export)

    st.dataframe(
        df,
        use_container_width=True
    )

    st.download_button(

        "📥 Download Submission CSV",

        df.to_csv(index=False),

        "submission.csv",

        "text/csv"

    )

    st.divider()

    st.subheader("⚙️ Ranking Pipeline")

    st.code("""

Job Description
        │
        ▼
Keyword Extraction
        │
        ▼
Feature Ranking
(10,000 Candidates)
        │
        ▼
Top 300 Candidates
        │
        ▼
Semantic Re-ranking
(Sentence Transformer)
        │
        ▼
Top 100 Candidates
        │
        ▼
Explainable AI Ranking

""")
    