from src.data.data_loader import load_students, load_jobs
from src.nlp.skill_extractor import extract_skills
from src.analysis.skill_matcher import match_skills
from src.analysis.skill_gap_analyzer import analyze_skill_gaps


def main():

    students = load_students()
    jobs = load_jobs()

    # Select student and job
    student = students.iloc[0]
    job = jobs.iloc[0]

    # Student skills
    student_skills = [
        skill.strip()
        for skill in student["skills"].split(";")
    ]

    # Extract job skills
    job_skills = extract_skills(
        job["description"]
    )

    # Match skills
    match_result = match_skills(
        student_skills,
        job_skills
    )

    # Analyze missing skills
    gaps = analyze_skill_gaps(
        match_result["missing"]
    )

    print("=" * 70)
    print("MODULE 4 - SKILL GAP ANALYSIS")
    print("=" * 70)

    print(f"\nStudent : {student['name']}")
    print(f"Target Job : {job['job_title']}")
    print(f"Company : {job['company']}")

    print(
        f"\nCurrent Match Score: "
        f"{match_result['match_score']}%"
    )

    print("\nSkill Gaps:")

    if not gaps:
        print("✓ No skill gaps identified!")

    else:

        for gap in gaps:

            print("\n----------------------------------------")

            print(
                f"Missing Skill : {gap['skill']}"
            )

            print(
                f"Category      : {gap['category']}"
            )

            print(
                f"Priority      : {gap['priority']}"
            )

            print(
                f"Recommendation: "
                f"{gap['recommendation']}"
            )


if __name__ == "__main__":
    main()