import re

from features import candidate_text


def generate_reasoning(candidate, jd_keywords):

    text = candidate_text(candidate)

    headline = candidate["profile"].get("headline", "")

    reasons = []

    # -----------------------------------
    # Experience
    # -----------------------------------

    match = re.search(r'(\d+(\.\d+)?)\+?\s*yrs', headline.lower())

    years = None

    if match:
        years = match.group(1)
        reasons.append(f"{years}+ years of experience")

    # -----------------------------------
    # Matched JD Skills
    # -----------------------------------

    skill_names = {
        "search": "Search",
        "retrieval": "Retrieval",
        "ranking": "Ranking",
        "recommendation": "Recommendation Systems",
        "recommendation systems": "Recommendation Systems",
        "nlp": "Natural Language Processing",
        "llm": "LLMs",
        "embedding": "Embeddings",
        "embeddings": "Embeddings",
        "python": "Python",
        "tensorflow": "TensorFlow",
        "pytorch": "PyTorch",
        "docker": "Docker",
        "kubernetes": "Kubernetes",
        "mlops": "MLOps",
        "production": "Production ML"
    }

    matched = []

    for keyword in jd_keywords:

        if keyword in text:

            display = skill_names.get(keyword, keyword.title())

            if display not in matched:
                matched.append(display)

    # -----------------------------------
    # Build Reasoning
    # -----------------------------------

    reasoning = headline

    if years:

        reasoning += f" with {years}+ years of experience"

    if matched:

        reasoning += (
            ". Demonstrates expertise in "
            + ", ".join(matched[:5])
        )

        reasoning += (
            ", aligning well with the key requirements of the Job Description."
        )

    else:

        reasoning += (
            ". Shows relevant technical background with partial alignment to the Job Description."
        )

    return reasoning
