BLOCKED_PHRASES = [
    "fake experience",
    "fake resume",
    "fake certificate",
    "fake internship",
    "cheat interview",
    "lie on resume",
]


def validate_prompt(prompt: str):
    text = prompt.lower()

    for phrase in BLOCKED_PHRASES:
        if phrase in text:
            raise ValueError(
                "This request violates AI safety guidelines."
            )