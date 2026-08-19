import re


def clean_text(text: str) -> str:
    """
    Basic text cleaning for review sentiment classification.

    The goal is to remove obvious noise while preserving
    sentiment-related information.
    """

    if not isinstance(text, str):
        return ""

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove leading/trailing whitespace
    text = text.strip()

    return text