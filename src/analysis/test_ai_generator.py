"""
TEST MODULE - AI GENERATION
"""

from .ai_generator import AIGenerator


def main():

    print("=" * 70)
    print("MODULE 6 - AI GENERATION")
    print("=" * 70)

    generator = AIGenerator()

    # ---------------------------------------------------------
    # STUDENT DATA
    # ---------------------------------------------------------

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
        },
        {
            "name": "Fraud Detection",
            "description": "Machine learning fraud detection project",
            "technologies": [
                "Python",
                "Scikit-learn"
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

    # ---------------------------------------------------------
    # GENERATE ANALYSIS
    # ---------------------------------------------------------

    result = generator.generate_complete_analysis(
        name=name,
        target_job=target_job,
        skills=skills,
        missing_skills=missing_skills,
        education=education,
        projects=projects,
        ats_scores=ats_scores
    )

    # ---------------------------------------------------------
    # DISPLAY SUMMARY
    # ---------------------------------------------------------

    print("\nPROFESSIONAL SUMMARY")
    print("-" * 70)

    print(result["professional_summary"])

    # ---------------------------------------------------------
    # SKILL RECOMMENDATIONS
    # ---------------------------------------------------------

    print("\nSKILL RECOMMENDATIONS")
    print("-" * 70)

    for item in result["skill_recommendations"]:
        print(f"• {item}")

    # ---------------------------------------------------------
    # PROJECT SUGGESTIONS
    # ---------------------------------------------------------

    print("\nPROJECT SUGGESTIONS")
    print("-" * 70)

    for item in result["project_suggestions"]:
        print(f"• {item}")

    # ---------------------------------------------------------
    # RESUME IMPROVEMENTS
    # ---------------------------------------------------------

    print("\nRESUME IMPROVEMENTS")
    print("-" * 70)

    for item in result["resume_improvements"]:
        print(f"• {item}")

    print("=" * 70)


if __name__ == "__main__":
    main()