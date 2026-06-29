from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


print("Loading Sentence Transformer...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

print("Model Loaded Successfully")


def semantic_similarity(jd_text, candidate_text):

    jd_embedding = model.encode(
        jd_text,
        normalize_embeddings=True
    )

    candidate_embedding = model.encode(
        candidate_text,
        normalize_embeddings=True
    )

    similarity = cosine_similarity(
        [jd_embedding],
        [candidate_embedding]
    )[0][0]

    return float(similarity)
