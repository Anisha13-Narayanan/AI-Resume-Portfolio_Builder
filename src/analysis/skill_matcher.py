from typing import List, Dict


def normalize_skills(skills: List[str]) -> set:
    """
    Normalize skill names for reliable comparison.
    """

    return {
        skill.strip().lower()
        for skill in skills
        if skill and skill.strip()
    }


def match_skills(
    student_skills: List[str],
    job_skills: List[str]
) -> Dict:
    """
    Compare student skills with job-required skills.

    Returns:
        matched skills
        missing skills
        extra skills
        match score
    """

    student_normalized = normalize_skills(student_skills)
    job_normalized = normalize_skills(job_skills)

    # Skills present in both
    matched = student_normalized.intersection(job_normalized)

    # Skills required by job but missing from student
    missing = job_normalized - student_normalized

    # Student skills not required by this particular job
    extra = student_normalized - job_normalized

    # Avoid division by zero
    if len(job_normalized) > 0:
        match_score = (
            len(matched) / len(job_normalized)
        ) * 100
    else:
        match_score = 0.0

    # Preserve readable capitalization
    skill_display = {
        skill.lower(): skill
        for skill in student_skills + job_skills
    }

    return {
        "matched": sorted(
            [skill_display[s] for s in matched]
        ),
        "missing": sorted(
            [skill_display[s] for s in missing]
        ),
        "extra": sorted(
            [skill_display[s] for s in extra]
        ),
        "match_score": round(match_score, 2)
    }