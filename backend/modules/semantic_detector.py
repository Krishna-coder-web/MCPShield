from sentence_transformers import SentenceTransformer
from sentence_transformers import util

model = SentenceTransformer("all-MiniLM-L6-v2")


def similarity(prompt, examples):

    prompt_embedding = model.encode(
        prompt,
        convert_to_tensor=True
    )

    highest_score = 0

    for example in examples:

        example_embedding = model.encode(
            example,
            convert_to_tensor=True
        )

        score = util.cos_sim(
            prompt_embedding,
            example_embedding
        ).item()

        highest_score = max(
            highest_score,
            score
        )

    return highest_score