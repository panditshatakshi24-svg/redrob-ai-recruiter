from semantic import semantic_similarity

jd = """
Looking for an AI Engineer
with Search,
Ranking,
Retrieval,
NLP,
Recommendation Systems
"""

candidate = """
Recommendation Systems Engineer
Search
Ranking
Retrieval
Production ML
"""

print(
    semantic_similarity(
        jd,
        candidate
    )
)
