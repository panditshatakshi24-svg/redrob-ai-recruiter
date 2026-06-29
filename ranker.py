from data_loader import load_candidates

from features import (
    feature_score,
    experience_score,
    extract_keywords,
    candidate_text
)

from semantic import semantic_similarity
from reasoning import generate_reasoning


def rank_candidates(jd):

    candidates = load_candidates()

    keywords = extract_keywords(jd)

    stage1 = []

    print("=" * 60)
    print("Stage 1 : Feature Ranking")
    print("=" * 60)

    for candidate in candidates:

        score = feature_score(candidate, keywords)
        score += experience_score(candidate)

        stage1.append(
            (
                candidate,
                score
            )
        )

    stage1.sort(
        key=lambda x: x[1],
        reverse=True
    )

    top300 = stage1[:300]

    print(f"Retrieved Top {len(top300)} candidates")

    print("=" * 60)
    print("Stage 2 : Semantic Re-ranking")
    print("=" * 60)

    final_results = []

    for candidate, feature in top300:

        text = candidate_text(candidate)

        semantic = semantic_similarity(
            jd,
            text
        )

        final_score = (
            feature * 0.80
            +
            semantic * 60
        )

        reasoning = generate_reasoning(
            candidate,
            keywords
        )

        final_results.append(

            {

                "candidate_id":
                    candidate["candidate_id"],

                "headline":
                    candidate["profile"]["headline"],

                "score":
                    round(final_score, 2),

                "semantic_score":
                    round(semantic * 100, 2),

                "feature_score":
                    feature,

                "reasoning":
                    reasoning

            }

        )

    final_results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    print(f"Final Top {len(final_results[:100])} Candidates Ready")

    return final_results[:100]
