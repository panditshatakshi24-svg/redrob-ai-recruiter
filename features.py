import re


# ==========================================================
# Build Candidate Text
# ==========================================================
def candidate_text(candidate):

    text = ""

    profile = candidate.get("profile", {})

    text += profile.get("headline", "") + " "
    text += profile.get("summary", "") + " "

    for skill in candidate.get("skills", []):
        text += skill.get("name", "") + " "

    for job in candidate.get("career_history", []):
        text += job.get("title", "") + " "
        text += job.get("description", "") + " "

    return text.lower()


# ==========================================================
# Extract JD Keywords
# ==========================================================
def extract_keywords(jd):

    jd = jd.lower()

    keywords = [

        "machine learning",
        "ml",
        "ai",
        "nlp",
        "search",
        "retrieval",
        "ranking",
        "recommendation",
        "recommendation systems",
        "vector search",
        "semantic search",
        "embedding",
        "embeddings",
        "llm",
        "rag",
        "transformer",
        "bert",
        "python",
        "tensorflow",
        "pytorch",
        "production",
        "mlops",
        "docker",
        "kubernetes"

    ]

    found = []

    for word in keywords:

        if word in jd:
            found.append(word)

    return found


# ==========================================================
# Feature Score
# ==========================================================
def feature_score(candidate, jd_keywords):

    text = candidate_text(candidate)

    headline = candidate["profile"]["headline"].lower()

    score = 0

    # ------------------------------------------------------
    # Keyword Weights
    # ------------------------------------------------------

    weights = {

        "search": 40,
        "retrieval": 40,
        "ranking": 35,
        "recommendation systems": 40,
        "recommendation": 25,
        "vector search": 35,
        "semantic search": 35,
        "nlp": 30,
        "machine learning": 25,
        "ml": 20,
        "ai": 15,
        "llm": 20,
        "rag": 25,
        "embedding": 25,
        "embeddings": 25,
        "transformer": 20,
        "bert": 20,
        "python": 10,
        "tensorflow": 15,
        "pytorch": 15,
        "production": 25,
        "docker": 15,
        "kubernetes": 15,
        "mlops": 20

    }

    for keyword in jd_keywords:

        if keyword in text:

            score += weights.get(keyword, 10)

    # ------------------------------------------------------
    # Core JD Skill Boost
    # ------------------------------------------------------

    core_terms = [

        "search",
        "retrieval",
        "ranking",
        "recommendation systems"

    ]

    for term in core_terms:

        if term in text:

            score += 30

    # ------------------------------------------------------
    # Dynamic Role Bonus
    # ------------------------------------------------------

    role_bonus = {

        "recommendation systems engineer": 150,
        "search engineer": 145,
        "recommendation engineer": 140,
        "senior nlp engineer": 140,
        "nlp engineer": 135,
        "machine learning engineer": 130,
        "ml engineer": 125,
        "applied ml engineer": 125,
        "senior ai engineer": 120,
        "ai engineer": 115,
        "ai research engineer": 110,
        "data scientist": 95,
        "ai specialist": 90,
        "computer vision engineer": 70,
        "backend engineer": 35,
        "software engineer": 30,
        "data engineer": 30

    }

    # ----------------------------
    # Adapt role bonus to JD
    # ----------------------------

    if "search" in jd_keywords:
        role_bonus["search engineer"] += 25

    if "recommendation" in jd_keywords:
        role_bonus["recommendation systems engineer"] += 25

    if "ranking" in jd_keywords:
        role_bonus["recommendation systems engineer"] += 15

    if "nlp" in jd_keywords:
        role_bonus["nlp engineer"] += 20
        role_bonus["senior nlp engineer"] += 20

    for role, bonus in role_bonus.items():

        if role in headline:

            score += bonus

            break

    # ------------------------------------------------------
    # Production Bonus
    # ------------------------------------------------------

    production_keywords = [

        "production",
        "deployment",
        "serving",
        "distributed systems",
        "mlops",
        "kubernetes",
        "docker",
        "api",
        "pipeline"

    ]

    for word in production_keywords:

        if word in text:

            score += 10

    return score


# ==========================================================
# Experience Score
# ==========================================================
def experience_score(candidate):

    score = 0

    headline = candidate["profile"]["headline"].lower()

    match = re.search(r'(\d+(\.\d+)?)\+?\s*yrs', headline)

    if match:

        years = float(match.group(1))

        if years >= 10:

            score += 50

        elif years >= 8:

            score += 40

        elif years >= 6:

            score += 30

        elif years >= 4:

            score += 20

        elif years >= 2:

            score += 10

    return score
