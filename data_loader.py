import json
import os
import gdown

FILE_ID = "1fMksbaaVK4py0hLKmy5FOoJ2BymplCmQ"
DATASET_PATH = "data/candidates.jsonl"


def download_dataset():

    os.makedirs("data", exist_ok=True)

    url = f"https://drive.google.com/uc?id={FILE_ID}"

    print("Downloading dataset...")

    gdown.download(
        url,
        DATASET_PATH,
        quiet=False
    )

    print("Dataset downloaded successfully.")


def load_candidates(limit=10000):

    if not os.path.exists(DATASET_PATH):
        download_dataset()

    candidates = []

    with open(DATASET_PATH, encoding="utf-8") as f:

        for i, line in enumerate(f):

            if i >= limit:
                break

            candidates.append(json.loads(line))

    return candidates
