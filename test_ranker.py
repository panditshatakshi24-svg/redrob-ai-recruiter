from ranker import rank_candidates


jd = """

We are looking for an AI Engineer

Responsibilities

Search

Ranking

Retrieval

Recommendation Systems

Production ML

NLP

LLMs

"""

results = rank_candidates(jd)

print()

print("="*80)

print("TOP 20")

print("="*80)

for r in results[:20]:

    print(r)
    