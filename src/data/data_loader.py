from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data" / "raw"


def load_students():
    return pd.read_csv(DATA_DIR / "students.csv")


def load_jobs():
    return pd.read_csv(DATA_DIR / "job_descriptions.csv")


def load_skills():
    return pd.read_csv(DATA_DIR / "skills.csv")


def load_skill_categories():
    return pd.read_csv(DATA_DIR / "skill_categories.csv")


def load_skill_matching():
    return pd.read_csv(DATA_DIR / "skill_matching.csv")


if __name__ == "__main__":
    students = load_students()
    jobs = load_jobs()
    skills = load_skills()

    print("=" * 60)
    print("AI RESUME & PORTFOLIO BUILDER")
    print("=" * 60)

    print("\nStudents:")
    print(students.shape)

    print("\nJob descriptions:")
    print(jobs.shape)

    print("\nSkills:")
    print(skills.shape)

    print("\nSample students:")
    print(students[["student_id", "name", "education"]].head())

    print("\nSample jobs:")
    print(jobs[["job_id", "job_title", "company"]].head())