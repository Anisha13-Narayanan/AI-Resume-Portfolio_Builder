"""
TEST MODULE - GEMINI AI INTEGRATION
"""

from .ai_generator import AIGenerator


def main():

    print("=" * 70)
    print("MODULE 6B - GEMINI AI INTEGRATION")
    print("=" * 70)

    generator = AIGenerator()

    print("\nGemini available:", generator.ai_available)

    if not generator.ai_available:
        print("\nWARNING:")
        print("GEMINI_API_KEY was not found.")
        print("Check your .env file.")
        return

    name = "Aarav Menon"

    target_job = "Junior Data Analyst"

    skills = [
        "Python",
        "SQL",
        "Power BI",
        "Excel",
        "Pandas",
        "Statistics"
    ]

    missing_skills = [
        "Tableau",
        "Machine Learning"
    ]

    education = {
        "degree": "BSc Data Science",
        "field": "Data Science and Analytics",
        "institution": "ABC University",
        "graduation_year": "2027"
    }

    projects = [
        {
            "name": "Sales Dashboard",
            "description": "Interactive sales analysis dashboard",
            "technologies": [
                "Power BI",
                "Excel"
            ]
        },
        {
            "name": "Customer Analysis",
            "description": "Customer segmentation project",
            "technologies": [
                "Python",
                "Pandas"
            ]
        }
    ]

    ats_scores = {
        "skill_score": 75.0,
        "keyword_score": 77.78,
        "education_score": 100.0,
        "project_score": 100.0,
        "structure_score": 80.0,
        "completeness_score": 100.0,
        "final_ats_score": 83.56
    }

    print("\nConnecting to Gemini...")
    print("Generating AI analysis...")

    result = generator.generate_complete_ai_analysis(
        name=name,
        target_job=target_job,
        skills=skills,
        missing_skills=missing_skills,
        education=education,
        projects=projects,
        ats_scores=ats_scores
    )

    print("\n" + "=" * 70)
    print("AI PROFESSIONAL SUMMARY")
    print("=" * 70)

    print(result["professional_summary"])

    print("\n" + "=" * 70)
    print("AI SKILL RECOMMENDATIONS")
    print("=" * 70)

    print(result["skill_recommendations"])

    print("\n" + "=" * 70)
    print("AI PROJECT IMPROVEMENTS")
    print("=" * 70)

    for project in result["project_improvements"]:
        print(f"\n{project['name']}")
        print(project["improved_description"])

    print("\n" + "=" * 70)
    print("AI RESUME IMPROVEMENTS")
    print("=" * 70)

    print(result["resume_improvements"])

    print("\n" + "=" * 70)
    print("AI USED:", result["ai_used"])
    print("=" * 70)


if __name__ == "__main__":
    main()