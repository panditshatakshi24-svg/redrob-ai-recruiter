import json


def load_candidates(limit=10000):

    candidates = []

    with open("data/candidates.jsonl", encoding="utf-8") as f:

        for i, line in enumerate(f):

            if i >= limit:
                break

            candidates.append(json.loads(line))

    return candidates
