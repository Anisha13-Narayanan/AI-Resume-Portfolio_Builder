from src.data.data_loader import load_students, load_jobs
from src.nlp.skill_extractor import extract_skills
from src.analysis.skill_matcher import match_skills


def main():

    students = load_students()
    jobs = load_jobs()

    # Select first student
    student = students.iloc[0]

    # Select first job
    job = jobs.iloc[0]

    # Student skills
    student_skills = [
        skill.strip()
        for skill in student["skills"].split(";")
    ]

    # Extract required skills from job description
    job_skills = extract_skills(job["description"])

    # Match
    result = match_skills(
        student_skills,
        job_skills
    )

    print("=" * 70)
    print("MODULE 3 - SKILL MATCHING")
    print("=" * 70)

    print(f"\nStudent : {student['name']}")
    print(f"Job     : {job['job_title']}")
    print(f"Company : {job['company']}")

    print("\nStudent Skills:")
    for skill in student_skills:
        print(f"  • {skill}")

    print("\nRequired Job Skills:")
    for skill in job_skills:
        print(f"  • {skill}")

    print("\nMatched Skills:")
    for skill in result["matched"]:
        print(f"  ✓ {skill}")

    print("\nMissing Skills:")
    for skill in result["missing"]:
        print(f"  ✗ {skill}")

    print("\nAdditional Student Skills:")
    for skill in result["extra"]:
        print(f"  + {skill}")

    print(
        f"\nSkill Match Score: "
        f"{result['match_score']}%"
    )


if __name__ == "__main__":
    main()