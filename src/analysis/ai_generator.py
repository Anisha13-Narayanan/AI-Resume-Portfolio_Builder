"""
MODULE 6B - GEMINI AI GENERATION

Features:
- One Gemini request for complete resume analysis
- Gemini 2.0 Flash primary model
- Gemini 1.5 Flash fallback model
- Retry handling for temporary 503 / 429 errors
- Rule-based fallback if Gemini is unavailable
- Professional summary
- Skill recommendations
- Project improvements
- Resume improvements
"""

import os
import time
import json

from dotenv import load_dotenv
from google import genai


class AIGenerator:

    def __init__(self):
        """Initialize Gemini client."""

        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        self.client = None
        self.ai_available = False

        self.models = [
            "gemini-2.0-flash",
            "gemini-1.5-flash"
        ]

        if api_key:
            try:
                self.client = genai.Client(
                    api_key=api_key
                )

                self.ai_available = True

            except Exception as e:
                print(f"Gemini initialization error: {e}")
                self.ai_available = False

    # =========================================================
    # GEMINI API
    # =========================================================

    def generate_complete_with_gemini(
        self,
        name,
        target_job,
        skills,
        missing_skills,
        education,
        projects,
        ats_scores
    ):
        """
        Generate complete resume analysis
        using ONE Gemini API request.
        """

        if not self.ai_available:
            return None

        prompt = f"""
You are an expert ATS resume writer and career advisor.

Analyze the following student profile for the target job.

==============================
STUDENT
==============================

Name:
{name}

Target Job:
{target_job}

Skills:
{skills}

Missing Job Skills:
{missing_skills}

Education:
{education}

Projects:
{projects}

ATS Scores:
{ats_scores}

==============================
TASK
==============================

Generate:

1. Professional Summary
2. Skill Recommendations
3. Project Improvements
4. Resume Improvements

==============================
STRICT RULES
==============================

- Do not invent experience.
- Do not invent companies.
- Do not invent certifications.
- Do not invent achievements.
- Do not invent metrics.
- Do not claim missing skills as existing skills.
- Only use information supplied above.
- Make the content ATS-friendly.
- Keep the writing professional.
- Tailor everything to the target job.

==============================
OUTPUT FORMAT
==============================

Return ONLY valid JSON.

Use exactly this structure:

{{
    "professional_summary": "3-4 sentence professional summary",

    "skill_recommendations": [
        "recommendation 1",
        "recommendation 2",
        "recommendation 3"
    ],

    "project_improvements": [
        {{
            "name": "project name",
            "improved_description": "2-3 concise resume bullet points"
        }}
    ],

    "resume_improvements": [
        "improvement 1",
        "improvement 2",
        "improvement 3"
    ]
}}
"""

        # -----------------------------------------------------
        # TRY AVAILABLE MODELS
        # -----------------------------------------------------

        for model in self.models:

            print(
                f"\nTrying Gemini model: {model}"
            )

            # -------------------------------------------------
            # RETRY EACH MODEL
            # -------------------------------------------------

            for attempt in range(2):

                try:

                    response = (
                        self.client.models.generate_content(
                            model=model,
                            contents=prompt
                        )
                    )

                    if not response or not response.text:

                        print(
                            "Gemini returned an empty response."
                        )

                        break

                    text = response.text.strip()

                    # Remove Markdown JSON fences
                    if text.startswith("```json"):
                        text = text[7:]

                    elif text.startswith("```"):
                        text = text[3:]

                    if text.endswith("```"):
                        text = text[:-3]

                    text = text.strip()

                    # Convert JSON string to Python dictionary
                    result = json.loads(text)

                    print(
                        f"Gemini succeeded using {model}."
                    )

                    return result

                # -------------------------------------------------
                # INVALID JSON
                # -------------------------------------------------

                except json.JSONDecodeError:

                    print(
                        "Gemini returned invalid JSON."
                    )

                    break

                # -------------------------------------------------
                # API ERROR
                # -------------------------------------------------

                except Exception as e:

                    error_message = str(e)

                    print(
                        f"\nAttempt {attempt + 1}/2 failed:"
                    )

                    print(error_message)

                    # ---------------------------------------------
                    # 503 TEMPORARY ERROR
                    # ---------------------------------------------

                    if (
                        "503" in error_message
                        or "UNAVAILABLE" in error_message
                    ):

                        if attempt == 0:

                            print(
                                "Temporary Gemini service issue."
                            )

                            print(
                                "Retrying in 2 seconds..."
                            )

                            time.sleep(2)

                            continue

                        print(
                            f"{model} is currently unavailable."
                        )

                        break

                    # ---------------------------------------------
                    # 429 RATE LIMIT
                    # ---------------------------------------------

                    if (
                        "429" in error_message
                        or "RESOURCE_EXHAUSTED"
                        in error_message
                    ):

                        if attempt == 0:

                            print(
                                "Gemini rate limit reached."
                            )

                            print(
                                "Retrying in 5 seconds..."
                            )

                            time.sleep(5)

                            continue

                        print(
                            f"{model} rate limit reached."
                        )

                        break

                    # ---------------------------------------------
                    # OTHER ERROR
                    # ---------------------------------------------

                    print(
                        "Gemini request failed."
                    )

                    break

        # ---------------------------------------------------------
        # ALL MODELS FAILED
        # ---------------------------------------------------------

        print(
            "\nAll Gemini models are currently unavailable."
        )

        print(
            "Using rule-based fallback."
        )

        return None

    # =========================================================
    # COMPLETE AI ANALYSIS
    # =========================================================

    def generate_complete_ai_analysis(
        self,
        name,
        target_job,
        skills,
        missing_skills,
        education,
        projects,
        ats_scores
    ):
        """
        Generate complete AI resume analysis.
        """

        print(
            "\nGenerating complete AI analysis..."
        )

        # -----------------------------------------------------
        # TRY GEMINI
        # -----------------------------------------------------

        if self.ai_available:

            result = self.generate_complete_with_gemini(
                name=name,
                target_job=target_job,
                skills=skills,
                missing_skills=missing_skills,
                education=education,
                projects=projects,
                ats_scores=ats_scores
            )

            if result:

                return {
                    "professional_summary":
                        result.get(
                            "professional_summary",
                            ""
                        ),

                    "skill_recommendations":
                        result.get(
                            "skill_recommendations",
                            []
                        ),

                    "project_improvements":
                        result.get(
                            "project_improvements",
                            []
                        ),

                    "resume_improvements":
                        result.get(
                            "resume_improvements",
                            []
                        ),

                    "ai_used": True,

                    "model": "Gemini"
                }

        # -----------------------------------------------------
        # FALLBACK
        # -----------------------------------------------------

        return self.generate_fallback_analysis(
            name=name,
            target_job=target_job,
            skills=skills,
            missing_skills=missing_skills,
            education=education,
            projects=projects,
            ats_scores=ats_scores
        )

    # =========================================================
    # FALLBACK ANALYSIS
    # =========================================================

    def generate_fallback_analysis(
        self,
        name,
        target_job,
        skills,
        missing_skills,
        education,
        projects,
        ats_scores
    ):
        """
        Rule-based fallback.
        """

        summary = self.generate_summary(
            name=name,
            target_job=target_job,
            skills=skills,
            education=education,
            projects=projects
        )

        skill_recommendations = (
            self.generate_skill_recommendations(
                matched_skills=skills,
                missing_skills=missing_skills
            )
        )

        project_improvements = []

        for project in projects:

            project_improvements.append(
                {
                    "name": project.get(
                        "name",
                        "Project"
                    ),

                    "improved_description":
                        self.generate_project_fallback(
                            project
                        )
                }
            )

        resume_improvements = (
            self.generate_resume_improvements(
                ats_scores
            )
        )

        return {
            "professional_summary":
                summary,

            "skill_recommendations":
                skill_recommendations,

            "project_improvements":
                project_improvements,

            "resume_improvements":
                resume_improvements,

            "ai_used": False,

            "model":
                "Rule-based fallback"
        }

    # =========================================================
    # FALLBACK SUMMARY
    # =========================================================

    def generate_summary(
        self,
        name,
        target_job,
        skills,
        education,
        projects
    ):
        """Generate rule-based professional summary."""

        skill_text = ", ".join(
            skills[:6]
        )

        degree = education.get(
            "degree",
            "Data Science student"
        )

        project_count = len(projects)

        project_word = (
            "project"
            if project_count == 1
            else "projects"
        )

        return (
            f"{degree} with hands-on experience in "
            f"{skill_text}. Developed "
            f"{project_count} relevant {project_word} "
            f"and seeking a {target_job} role. "
            f"Interested in applying analytical, "
            f"technical, and problem-solving skills "
            f"to real-world data challenges."
        )

    # =========================================================
    # FALLBACK SKILL RECOMMENDATIONS
    # =========================================================

    def generate_skill_recommendations(
        self,
        matched_skills,
        missing_skills
    ):
        """Generate rule-based skill recommendations."""

        if not missing_skills:

            return [
                "Your skills align well with "
                "the target job."
            ]

        return [
            (
                f"Consider learning or demonstrating "
                f"{skill} if it is relevant to your "
                f"experience."
            )
            for skill in missing_skills
        ]

    # =========================================================
    # FALLBACK PROJECT DESCRIPTION
    # =========================================================

    def generate_project_fallback(
        self,
        project
    ):
        """Generate rule-based project improvement."""

        name = project.get(
            "name",
            "the project"
        )

        technologies = project.get(
            "technologies",
            []
        )

        if technologies:

            technology_text = ", ".join(
                str(item)
                for item in technologies
            )

            return (
                f"• Developed {name} using "
                f"{technology_text}.\n"
                f"• Applied technical and analytical "
                f"skills to complete the project."
            )

        return (
            f"• Developed {name} as a practical "
            f"data-focused project.\n"
            f"• Applied analytical and "
            f"problem-solving skills."
        )

    # =========================================================
    # FALLBACK ATS IMPROVEMENTS
    # =========================================================

    def generate_resume_improvements(
        self,
        ats_scores
    ):
        """Generate rule-based ATS improvements."""

        improvements = []

        skill_score = ats_scores.get(
            "skill_score",
            0
        )

        keyword_score = ats_scores.get(
            "keyword_score",
            0
        )

        education_score = ats_scores.get(
            "education_score",
            0
        )

        project_score = ats_scores.get(
            "project_score",
            0
        )

        structure_score = ats_scores.get(
            "structure_score",
            0
        )

        completeness_score = ats_scores.get(
            "completeness_score",
            0
        )

        if skill_score < 70:

            improvements.append(
                "Improve alignment between your "
                "skills and target job requirements."
            )

        if keyword_score < 70:

            improvements.append(
                "Include relevant keywords from "
                "the target job description."
            )

        if education_score < 70:

            improvements.append(
                "Complete the education section."
            )

        if project_score < 70:

            improvements.append(
                "Add more relevant projects and "
                "mention the technologies used."
            )

        if structure_score < 80:

            improvements.append(
                "Improve resume structure by adding "
                "important sections."
            )

        if completeness_score < 80:

            improvements.append(
                "Complete missing resume information."
            )

        if not improvements:

            improvements.append(
                "Your resume has strong overall "
                "ATS compatibility."
            )

        return improvements


# =============================================================
# DIRECT TEST
# =============================================================

if __name__ == "__main__":

    print("=" * 70)
    print("AI GENERATOR MODULE TEST")
    print("=" * 70)

    generator = AIGenerator()

    print(
        f"\nGemini available: "
        f"{generator.ai_available}"
    )

    result = generator.generate_complete_with_gemini(
        name="Aarav Menon",
        target_job="Junior Data Analyst",
        skills=[
            "Python",
            "SQL",
            "Power BI",
            "Excel",
            "Pandas",
            "Statistics"
        ],
        missing_skills=[
            "Tableau",
            "Machine Learning"
        ],
        education={
            "degree": "BSc Data Science",
            "field": "Data Science and Analytics",
            "institution": "ABC University",
            "graduation_year": "2027"
        },
        projects=[
            {
                "name": "Sales Dashboard",
                "description":
                    "Interactive sales analysis dashboard",
                "technologies": [
                    "Power BI",
                    "Excel"
                ]
            }
        ],
        ats_scores={
            "skill_score": 75.0,
            "keyword_score": 77.78,
            "education_score": 100.0,
            "project_score": 100.0,
            "structure_score": 80.0,
            "completeness_score": 100.0,
            "final_ats_score": 83.56
        }
    )

    if result:

        print("\nAI RESULT")
        print("=" * 70)

        print("\nProfessional Summary:")
        print(
            result.get(
                "professional_summary",
                ""
            )
        )

        print("\nSkill Recommendations:")

        for item in result.get(
            "skill_recommendations",
            []
        ):
            print(f"• {item}")

        print("\nProject Improvements:")

        for project in result.get(
            "project_improvements",
            []
        ):
            print(
                f"\n{project.get('name', 'Project')}"
            )

            print(
                project.get(
                    "improved_description",
                    ""
                )
            )

        print("\nResume Improvements:")

        for item in result.get(
            "resume_improvements",
            []
        ):
            print(f"• {item}")

    else:

        print(
            "\nGemini is currently unavailable."
        )

        print(
            "The rule-based fallback can be used "
            "by the main application."
        )

    print("\n" + "=" * 70)