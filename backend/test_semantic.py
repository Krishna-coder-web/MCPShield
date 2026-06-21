from modules.semantic_detector import similarity

examples = [
    "export customer records"
]

prompt = "retrieve customer database"

score = similarity(
    prompt,
    examples
)

print(score)