def normalize(text: str):

    text = text.lower()

    replacements = {
        "0": "o",
        "1": "i",
        "3": "e",
        "4": "a",
        "5": "s",
        "@": "a",
        "$": "s",
        "!": "i"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text