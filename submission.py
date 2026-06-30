import pandas as pd
from ranker import rank_candidates

jd = """
PASTE THE OFFICIAL REDROB JOB DESCRIPTION HERE
"""

results = rank_candidates(jd)

submission = []

for rank, candidate in enumerate(results, start=1):

    submission.append({
        "candidate_id": candidate["candidate_id"],
        "rank": rank,
        "score": candidate["score"],
        "reasoning": candidate["reasoning"]
    })

df = pd.DataFrame(submission)

df.to_csv(
    "YOUR_TEAM_ID.csv",
    index=False
)

print(df.head())
print("Saved successfully!")