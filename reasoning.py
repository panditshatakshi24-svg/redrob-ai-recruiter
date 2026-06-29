from features import candidate_text


def generate_reasoning(candidate, jd_keywords):

    text = candidate_text(candidate)

    reasons = []

    important = [
        "search",
        "retrieval",
        "ranking",
        "recommendation",
        "recommendation systems",
        "nlp",
        "llm",
        "embedding",
        "embeddings",
        "python",
        "production"
    ]

    for skill in important:

        if skill in text:
            reasons.append(skill.title())

    headline = candidate["profile"]["headline"]

    summary = (
        f"{headline}. "
        f"Matched Skills: {', '.join(reasons[:5])}."
    )

    return summary
