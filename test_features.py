from data_loader import load_candidates
from features import extract_keywords
from features import feature_score

candidates = load_candidates()

jd = """
Looking for an AI Engineer with
Search
Ranking
Retrieval
NLP
Recommendation Systems
"""

keywords = extract_keywords(jd)

print(keywords)

print(feature_score(candidates[0], keywords))
print(feature_score(candidates[1], keywords))
print(feature_score(candidates[2], keywords))
