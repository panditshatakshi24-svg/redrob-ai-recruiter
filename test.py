from data_loader import load_candidates

candidates = load_candidates()

print(len(candidates))
print(candidates[0]["candidate_id"])
print(candidates[0]["profile"]["headline"])
