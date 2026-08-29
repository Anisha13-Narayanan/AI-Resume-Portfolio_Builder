import re


def clean_text(text: str) -> str:
    """
    Clean job description text for NLP processing.
    """

    if not isinstance(text, str):
        return ""

    # Convert to lowercase
    text = text.lower()

    # Replace special characters with spaces
    text = re.sub(r"[^a-zA-Z0-9+#.\s]", " ", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text