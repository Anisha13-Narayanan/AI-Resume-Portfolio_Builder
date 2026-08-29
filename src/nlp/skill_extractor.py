from pathlib import Path
import re
import pandas as pd

from src.nlp.text_preprocessor import clean_text


BASE_DIR = Path(__file__).resolve().parents[2]
SKILLS_FILE = BASE_DIR / "data" / "raw" / "skills.csv"


def load_skill_dictionary():
    """
    Load the project's master skill dictionary.
    """

    skills_df = pd.read_csv(SKILLS_FILE)

    skills = (
        skills_df["skill_name"]
        .dropna()
        .astype(str)
        .tolist()
    )

    return skills


def skill_exists(text: str, skill: str) -> bool:
    """
    Check whether a complete skill appears in the text.

    Word boundaries prevent false matches such as:
    R -> appearing inside 'for'.
    """

    cleaned_skill = clean_text(skill)

    if not cleaned_skill:
        return False

    # Escape special regex characters such as +, #, .
    pattern = r"(?<!\w)" + re.escape(cleaned_skill) + r"(?!\w)"

    return re.search(
        pattern,
        text,
        flags=re.IGNORECASE
    ) is not None


def extract_skills(text: str):
    """
    Extract known skills from a piece of text.
    """

    if not text:
        return []

    cleaned_text = clean_text(text)

    skills = load_skill_dictionary()

    found_skills = []

    for skill in skills:

        if skill_exists(cleaned_text, skill):
            found_skills.append(skill)

    # Remove duplicates while preserving order
    found_skills = list(dict.fromkeys(found_skills))

    return found_skills


if __name__ == "__main__":

    sample_job = """
    We are looking for a Junior Data Analyst.
    The candidate should have strong knowledge of Python,
    SQL, Excel, Power BI and Statistics.
    Experience with Pandas and data visualization is preferred.
    """

    extracted_skills = extract_skills(sample_job)

    print("=" * 60)
    print("NLP SKILL EXTRACTION")
    print("=" * 60)

    print("\nJob Description:")
    print(sample_job)

    print("\nExtracted Skills:")

    for skill in extracted_skills:
        print(f"✓ {skill}")

    print(f"\nTotal Skills Found: {len(extracted_skills)}")