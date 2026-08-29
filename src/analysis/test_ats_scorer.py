"""
TEST MODULE - ATS SCORING
"""

from .ats_scorer import ATSScorer


def main():

    print("=" * 70)
    print("MODULE 5 - ATS STYLE SCORING")
    print("=" * 70)

    scorer = ATSScorer()

    # ---------------------------------------------------------
    # STUDENT DATA
    # ---------------------------------------------------------

    matched_skills = [
        "Python",
        "SQL",
        "Power BI",
        "Excel",
        "Pandas",
        "Statistics"
    ]

    required_skills = [
        "Python",
        "SQL",
        "Power BI",
        "Excel",
        "Pandas",
        "Statistics",
        "Tableau",
        "Machine Learning"
    ]

    resume_text = """
    Data Science student with experience in Python, SQL,
    Power BI, Excel, Pandas and Statistics.
    Experienced in data analysis, visualization,
    machine learning and dashboard development.
    """

    job_description = """
    Junior Data Analyst required with Python, SQL,
    Power BI, Excel, Pandas, Statistics, Tableau,
    Machine Learning, data analysis and visualization.
    """

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
            "technologies": ["Power BI", "Excel"]
        },
        {
            "name": "Customer Analysis",
            "description": "Customer segmentation project",
            "technologies": ["Python", "Pandas"]
        },
        {
            "name": "Fraud Detection",
            "description": "Machine learning fraud detection project",
            "technologies": ["Python", "Scikit-learn"]
        }
    ]

    resume = {
        "name": "Aarav Menon",
        "email": "aarav@example.com",
        "phone": "9876543210",
        "summary": "Data Science student",
        "skills": matched_skills,
        "education": education,
        "projects": projects,
        "experience": None
    }

    # ---------------------------------------------------------
    # CALCULATE SCORE
    # ---------------------------------------------------------

    scores = scorer.calculate_ats_score(
        matched_skills=matched_skills,
        required_skills=required_skills,
        resume_text=resume_text,
        job_description=job_description,
        education=education,
        projects=projects,
        resume=resume
    )

    # ---------------------------------------------------------
    # DISPLAY RESULTS
    # ---------------------------------------------------------

    print("\nATS SCORE BREAKDOWN")
    print("-" * 70)

    print(f"Skill Match Score    : {scores['skill_score']}%")
    print(f"Keyword Score        : {scores['keyword_score']}%")
    print(f"Education Score      : {scores['education_score']}%")
    print(f"Project Score        : {scores['project_score']}%")
    print(f"Structure Score      : {scores['structure_score']}%")
    print(f"Completeness Score   : {scores['completeness_score']}%")

    print("-" * 70)

    print(
        f"FINAL ATS SCORE      : "
        f"{scores['final_ats_score']}/100"
    )

    # ---------------------------------------------------------
    # RECOMMENDATIONS
    # ---------------------------------------------------------

    recommendations = scorer.generate_recommendations(scores)

    print("\nRECOMMENDATIONS")
    print("-" * 70)

    for recommendation in recommendations:
        print(f"• {recommendation}")

    print("=" * 70)


if __name__ == "__main__":
    main()