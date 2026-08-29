"""
MODULE 5 - ATS STYLE SCORING

Calculates an ATS-style resume score using:
- Skill matching
- Keyword matching
- Education
- Projects
- Resume structure
- Resume completeness
"""


class ATSScorer:

    def __init__(self):
        self.weights = {
            "skill_match": 40,
            "keywords": 20,
            "education": 10,
            "projects": 15,
            "structure": 10,
            "completeness": 5
        }

    # ---------------------------------------------------------
    # 1. SKILL MATCH SCORE
    # ---------------------------------------------------------

    def calculate_skill_score(self, matched_skills, required_skills):
        """
        Calculate percentage of required skills matched.
        """

        if not required_skills:
            return 0

        matched = len(matched_skills)
        required = len(required_skills)

        score = (matched / required) * 100

        return round(min(score, 100), 2)

    # ---------------------------------------------------------
    # 2. KEYWORD SCORE
    # ---------------------------------------------------------

    def calculate_keyword_score(self, resume_text, job_description):
        """
        Calculate keyword overlap between resume and job description.
        """

        if not resume_text or not job_description:
            return 0

        resume_words = set(
            resume_text.lower().split()
        )

        job_words = set(
            job_description.lower().split()
        )

        # Remove punctuation
        resume_words = {
            word.strip(".,!?;:()[]{}")
            for word in resume_words
        }

        job_words = {
            word.strip(".,!?;:()[]{}")
            for word in job_words
        }

        common_words = resume_words.intersection(job_words)

        if not job_words:
            return 0

        score = (len(common_words) / len(job_words)) * 100

        return round(min(score, 100), 2)

    # ---------------------------------------------------------
    # 3. EDUCATION SCORE
    # ---------------------------------------------------------

    def calculate_education_score(self, education):
        """
        Basic education completeness check.
        """

        if not education:
            return 0

        score = 0

        if education.get("degree"):
            score += 40

        if education.get("field"):
            score += 30

        if education.get("institution"):
            score += 20

        if education.get("graduation_year"):
            score += 10

        return min(score, 100)

    # ---------------------------------------------------------
    # 4. PROJECT SCORE
    # ---------------------------------------------------------

    def calculate_project_score(self, projects):
        """
        Score based on number and completeness of projects.
        """

        if not projects:
            return 0

        project_count = len(projects)

        # Maximum score after 3 good projects
        base_score = min(project_count / 3, 1) * 70

        completeness_bonus = 0

        for project in projects:

            if project.get("name"):
                completeness_bonus += 5

            if project.get("description"):
                completeness_bonus += 5

            if project.get("technologies"):
                completeness_bonus += 5

        score = base_score + min(completeness_bonus, 30)

        return round(min(score, 100), 2)

    # ---------------------------------------------------------
    # 5. RESUME STRUCTURE SCORE
    # ---------------------------------------------------------

    def calculate_structure_score(self, resume):
        """
        Check whether important resume sections exist.
        """

        if not resume:
            return 0

        sections = [
            "summary",
            "skills",
            "education",
            "projects",
            "experience"
        ]

        available = 0

        for section in sections:
            if resume.get(section):
                available += 1

        score = (available / len(sections)) * 100

        return round(score, 2)

    # ---------------------------------------------------------
    # 6. COMPLETENESS SCORE
    # ---------------------------------------------------------

    def calculate_completeness_score(self, resume):
        """
        Check basic resume information.
        """

        if not resume:
            return 0

        fields = [
            "name",
            "email",
            "phone",
            "summary",
            "skills",
            "education",
            "projects"
        ]

        completed = 0

        for field in fields:
            if resume.get(field):
                completed += 1

        score = (completed / len(fields)) * 100

        return round(score, 2)

    # ---------------------------------------------------------
    # FINAL ATS SCORE
    # ---------------------------------------------------------

    def calculate_ats_score(
        self,
        matched_skills,
        required_skills,
        resume_text,
        job_description,
        education,
        projects,
        resume
    ):
        """
        Calculate complete ATS score.
        """

        skill_score = self.calculate_skill_score(
            matched_skills,
            required_skills
        )

        keyword_score = self.calculate_keyword_score(
            resume_text,
            job_description
        )

        education_score = self.calculate_education_score(
            education
        )

        project_score = self.calculate_project_score(
            projects
        )

        structure_score = self.calculate_structure_score(
            resume
        )

        completeness_score = self.calculate_completeness_score(
            resume
        )

        # Weighted calculation
        final_score = (
            skill_score * 0.40 +
            keyword_score * 0.20 +
            education_score * 0.10 +
            project_score * 0.15 +
            structure_score * 0.10 +
            completeness_score * 0.05
        )

        return {
            "skill_score": round(skill_score, 2),
            "keyword_score": round(keyword_score, 2),
            "education_score": round(education_score, 2),
            "project_score": round(project_score, 2),
            "structure_score": round(structure_score, 2),
            "completeness_score": round(completeness_score, 2),
            "final_ats_score": round(final_score, 2)
        }

    # ---------------------------------------------------------
    # RECOMMENDATIONS
    # ---------------------------------------------------------

    def generate_recommendations(self, scores):

        recommendations = []

        if scores["skill_score"] < 60:
            recommendations.append(
                "Improve skill alignment with the target job."
            )

        if scores["keyword_score"] < 60:
            recommendations.append(
                "Add important keywords from the job description."
            )

        if scores["education_score"] < 70:
            recommendations.append(
                "Complete the education section."
            )

        if scores["project_score"] < 70:
            recommendations.append(
                "Add more relevant projects with technologies used."
            )

        if scores["structure_score"] < 80:
            recommendations.append(
                "Improve resume structure and add missing sections."
            )

        if scores["completeness_score"] < 80:
            recommendations.append(
                "Complete missing personal and resume information."
            )

        if not recommendations:
            recommendations.append(
                "Resume has strong ATS compatibility."
            )

        return recommendations