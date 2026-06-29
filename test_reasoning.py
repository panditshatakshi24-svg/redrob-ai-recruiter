from data_loader import load_candidates
from features import extract_keywords
from reasoning import generate_reasoning

candidates = load_candidates(5)

jd = """
Looking for Search
Ranking
Recommendation Systems
NLP
"""

keywords = extract_keywords(jd)

print(generate_reasoning(candidates[0], keywords))
