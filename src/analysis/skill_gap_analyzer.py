from typing import List, Dict


# Skill categories and recommendations
SKILL_RECOMMENDATIONS = {

    "Python": {
        "category": "Programming",
        "priority": "High",
        "recommendation": "Learn Python fundamentals, functions, data structures and practical data analysis."
    },

    "SQL": {
        "category": "Database",
        "priority": "High",
        "recommendation": "Practice SELECT, JOIN, GROUP BY, subqueries and window functions."
    },

    "Excel": {
        "category": "Data Analysis",
        "priority": "Medium",
        "recommendation": "Practice formulas, pivot tables, lookups, charts and data cleaning."
    },

    "Power BI": {
        "category": "Data Visualization",
        "priority": "High",
        "recommendation": "Learn Power Query, data modeling, DAX and interactive dashboard development."
    },

    "Tableau": {
        "category": "Data Visualization",
        "priority": "Medium",
        "recommendation": "Practice calculated fields, filters, dashboards and interactive visualizations."
    },

    "Pandas": {
        "category": "Data Analysis",
        "priority": "High",
        "recommendation": "Practice data cleaning, filtering, grouping, merging and exploratory data analysis."
    },

    "NumPy": {
        "category": "Data Science",
        "priority": "Medium",
        "recommendation": "Learn NumPy arrays, indexing, vectorized operations and numerical calculations."
    },

    "Machine Learning": {
        "category": "Machine Learning",
        "priority": "High",
        "recommendation": "Study regression, classification, clustering, model evaluation and feature engineering."
    },

    "Statistics": {
        "category": "Statistics",
        "priority": "High",
        "recommendation": "Practice descriptive statistics, probability, hypothesis testing and correlation."
    },

    "Data Visualization": {
        "category": "Visualization",
        "priority": "Medium",
        "recommendation": "Learn how to select effective charts and communicate analytical insights clearly."
    },

    "Data Cleaning": {
        "category": "Data Analysis",
        "priority": "High",
        "recommendation": "Practice handling missing values, duplicates, inconsistent formats and outliers."
    },

    "Communication": {
        "category": "Soft Skills",
        "priority": "Medium",
        "recommendation": "Practice explaining analytical findings clearly to technical and non-technical audiences."
    },

    "Business Analysis": {
        "category": "Business",
        "priority": "Medium",
        "recommendation": "Learn requirements analysis, KPI identification, business problem solving and stakeholder analysis."
    },

    "Git": {
        "category": "Developer Tools",
        "priority": "Low",
        "recommendation": "Practice Git commits, branches, merges and GitHub repository management."
    },

    "GitHub": {
        "category": "Developer Tools",
        "priority": "Low",
        "recommendation": "Build a professional GitHub profile and maintain well-documented projects."
    }
}


def analyze_skill_gaps(missing_skills: List[str]) -> List[Dict]:
    """
    Analyze missing skills and generate personalized recommendations.
    """

    gaps = []

    for skill in missing_skills:

        # Find recommendation using case-insensitive matching
        recommendation = None

        for known_skill, details in SKILL_RECOMMENDATIONS.items():

            if known_skill.lower() == skill.lower():
                recommendation = details
                break

        # If skill isn't in our recommendation dictionary
        if recommendation is None:

            recommendation = {
                "category": "Other",
                "priority": "Medium",
                "recommendation": f"Develop practical knowledge and complete a project using {skill}."
            }

        gaps.append({
            "skill": skill,
            "category": recommendation["category"],
            "priority": recommendation["priority"],
            "recommendation": recommendation["recommendation"]
        })

    return gaps