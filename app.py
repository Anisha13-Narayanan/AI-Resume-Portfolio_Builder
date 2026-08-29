import streamlit as st

from src.data.data_loader import (
    load_students,
    load_jobs,
    load_skills
)

from src.nlp.skill_extractor import extract_skills

from src.analysis.skill_matcher import match_skills

from src.analysis.skill_gap_analyzer import (
    analyze_skill_gaps
)

from src.analysis.ats_scorer import ATSScorer

from src.analysis.ai_generator import AIGenerator

from src.documents.resume_generator import ResumeGenerator

from src.documents.pdf_generator import PDFResumeGenerator



# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Resume & Portfolio Builder",
    page_icon="📄",
    layout="wide"
)


# ============================================================
# CACHE DATA
# ============================================================

@st.cache_data
def get_project_data():

    students = load_students()
    jobs = load_jobs()
    skills = load_skills()

    return students, jobs, skills


# ============================================================
# TITLE
# ============================================================

st.title("📄 AI Resume & Portfolio Builder")

st.write(
    "Create a personalized ATS-friendly resume and portfolio "
    "based on your skills, projects, and target job."
)


# ============================================================
# LOAD DATA
# ============================================================

try:

    students, jobs, skills = get_project_data()

except Exception as e:

    st.error("❌ Error loading project data.")
    st.exception(e)
    st.stop()


# ============================================================
# DATASET OVERVIEW
# ============================================================

st.subheader("📊 Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Students", len(students))

with col2:
    st.metric("Job Descriptions", len(jobs))

with col3:
    st.metric("Skills", len(skills))


# ============================================================
# STUDENT PROFILES
# ============================================================

with st.expander("👨‍🎓 Student Profiles"):

    st.dataframe(
        students[
            [
                "student_id",
                "name",
                "education"
            ]
        ],
        use_container_width=True
    )


# ============================================================
# JOB ROLES
# ============================================================

with st.expander("💼 Available Job Roles"):

    st.dataframe(
        jobs[
            [
                "job_id",
                "job_title",
                "company"
            ]
        ],
        use_container_width=True
    )


# ============================================================
# MODULE 2
# NLP SKILL EXTRACTION
# ============================================================

st.divider()

st.header("🔎 Module 2 — NLP Skill Extraction")

selected_job_id_extraction = st.selectbox(
    "Select a Job",
    jobs["job_id"].tolist(),
    key="extraction_job"
)

selected_job_extraction = jobs[
    jobs["job_id"] == selected_job_id_extraction
].iloc[0]

st.write("### Job Description")

st.info(
    selected_job_extraction["description"]
)

if st.button(
    "🔍 Extract Skills",
    key="extract_skills_button"
):

    extracted_skills = extract_skills(
        selected_job_extraction["description"]
    )

    st.success(
        f"{len(extracted_skills)} skills detected"
    )

    if extracted_skills:

        columns = st.columns(3)

        for index, skill in enumerate(extracted_skills):

            with columns[index % 3]:

                st.success(
                    f"✓ {skill}"
                )

    else:

        st.warning(
            "No skills were detected."
        )


# ============================================================
# STUDENT + JOB SELECTION
# ============================================================

st.divider()

st.header("🎯 Student & Target Job")

student_id = st.selectbox(
    "Select Student",
    students["student_id"].tolist(),
    key="matching_student"
)

selected_student = students[
    students["student_id"] == student_id
].iloc[0]


job_id = st.selectbox(
    "Select Target Job",
    jobs["job_id"].tolist(),
    key="matching_job"
)

selected_job = jobs[
    jobs["job_id"] == job_id
].iloc[0]


# ============================================================
# STUDENT INFORMATION
# ============================================================

st.subheader("👤 Selected Student")

profile_col1, profile_col2 = st.columns(2)

with profile_col1:

    st.write(
        f"**Name:** {selected_student['name']}"
    )

    st.write(
        f"**Education:** {selected_student['education']}"
    )


with profile_col2:

    st.write("**Current Skills:**")

    student_skills_preview = [
        skill.strip()
        for skill in str(
            selected_student["skills"]
        ).split(";")
        if skill.strip()
    ]

    st.write(
        ", ".join(student_skills_preview)
    )


# ============================================================
# JOB INFORMATION
# ============================================================

st.subheader("💼 Target Job")

st.write(
    f"**Role:** {selected_job['job_title']}"
)

st.write(
    f"**Company:** {selected_job['company']}"
)

st.write(
    f"**Description:** {selected_job['description']}"
)


# ============================================================
# RESUME INFORMATION
# ============================================================

st.divider()

st.header("📝 Resume Information")

resume_col1, resume_col2 = st.columns(2)

with resume_col1:

    email = st.text_input(
        "Email",
        placeholder="student@email.com"
    )

    phone = st.text_input(
        "Phone",
        placeholder="+91 XXXXX XXXXX"
    )


with resume_col2:

    institution = st.text_input(
        "Institution",
        placeholder="University / College"
    )

    graduation_year = st.text_input(
        "Graduation Year",
        placeholder="2027"
    )


# ============================================================
# PROJECTS
# ============================================================

st.subheader("🚀 Projects")

project_count = st.number_input(
    "Number of Projects",
    min_value=0,
    max_value=10,
    value=2,
    step=1
)

projects = []

for i in range(project_count):

    st.markdown(
        f"#### Project {i + 1}"
    )

    project_col1, project_col2 = st.columns(2)

    with project_col1:

        project_name = st.text_input(
            "Project Name",
            key=f"project_name_{i}"
        )

    with project_col2:

        project_technologies = st.text_input(
            "Technologies",
            key=f"project_technologies_{i}",
            placeholder="Python, Pandas, Power BI"
        )

    project_description = st.text_area(
        "Project Description",
        key=f"project_description_{i}"
    )

    technologies = [
        item.strip()
        for item in project_technologies.split(",")
        if item.strip()
    ]

    projects.append(
        {
            "name": project_name,
            "description": project_description,
            "technologies": technologies
        }
    )


# ============================================================
# FAST ANALYSIS
# ============================================================

st.divider()

st.header("⚡ Resume Analysis")

st.caption(
    "This analysis does not call Gemini and should complete quickly."
)

analyze_button = st.button(
    "🚀 Analyze Resume",
    type="primary",
    use_container_width=True
)


if analyze_button:

    try:

        with st.spinner(
            "Running skill matching, gap analysis and ATS scoring..."
        ):

            # ==================================================
            # STUDENT SKILLS
            # ==================================================

            student_skills = [
                skill.strip()
                for skill in str(
                    selected_student["skills"]
                ).split(";")
                if skill.strip()
            ]


            # ==================================================
            # JOB SKILLS
            # ==================================================

            job_skills = extract_skills(
                selected_job["description"]
            )


            # ==================================================
            # SKILL MATCHING
            # ==================================================

            result = match_skills(
                student_skills,
                job_skills
            )


            # ==================================================
            # SKILL GAP ANALYSIS
            # ==================================================

            gaps = analyze_skill_gaps(
                result["missing"]
            )


            # ==================================================
            # EDUCATION
            # ==================================================

            education = {

                "degree": str(
                    selected_student["education"]
                ),

                "field": "",

                "institution": institution,

                "graduation_year": graduation_year
            }


            # ==================================================
            # RESUME OBJECT
            # ==================================================

            resume = {

                "name": str(
                    selected_student["name"]
                ),

                "email": email,

                "phone": phone,

                "summary": "",

                "skills": student_skills,

                "education": education,

                "projects": projects,

                "experience": ""
            }


            # ==================================================
            # RESUME TEXT
            # ==================================================

            resume_text_parts = [

                str(selected_student["name"]),

                str(selected_student["education"]),

                " ".join(student_skills)
            ]


            for project in projects:

                resume_text_parts.append(
                    str(project.get("name", ""))
                )

                resume_text_parts.append(
                    str(project.get("description", ""))
                )

                resume_text_parts.append(
                    " ".join(
                        project.get(
                            "technologies",
                            []
                        )
                    )
                )


            resume_text = " ".join(
                resume_text_parts
            )


            # ==================================================
            # ATS SCORING
            # ==================================================

            ats_scorer = ATSScorer()

            ats_scores = ats_scorer.calculate_ats_score(

                matched_skills=result["matched"],

                required_skills=job_skills,

                resume_text=resume_text,

                job_description=selected_job[
                    "description"
                ],

                education=education,

                projects=projects,

                resume=resume
            )


            # ==================================================
            # ATS RECOMMENDATIONS
            # ==================================================

            ats_recommendations = (
                ats_scorer.generate_recommendations(
                    ats_scores
                )
            )


            # ==================================================
            # SAVE RESULTS
            # ==================================================

            st.session_state["analysis_complete"] = True

            st.session_state["student"] = selected_student

            st.session_state["job"] = selected_job

            st.session_state["student_skills"] = student_skills

            st.session_state["job_skills"] = job_skills

            st.session_state["match_result"] = result

            st.session_state["skill_gaps"] = gaps

            st.session_state["ats_scores"] = ats_scores

            st.session_state[
                "ats_recommendations"
            ] = ats_recommendations

            st.session_state["resume"] = resume

            st.session_state["resume_text"] = resume_text

        st.success(
            "✅ Fast analysis completed!"
        )

    except Exception as e:

        st.error(
            "❌ Error during analysis."
        )

        st.exception(e)


# ============================================================
# DISPLAY FAST RESULTS
# ============================================================

if st.session_state.get(
    "analysis_complete",
    False
):

    result = st.session_state[
        "match_result"
    ]

    gaps = st.session_state[
        "skill_gaps"
    ]

    ats_scores = st.session_state[
        "ats_scores"
    ]

    ats_recommendations = st.session_state[
        "ats_recommendations"
    ]


    # ========================================================
    # MODULE 3
    # SKILL MATCHING
    # ========================================================

    st.divider()

    st.header(
        "🎯 Module 3 — Skill Matching"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Overall Match",
            f"{result['match_score']}%"
        )

    with col2:

        st.metric(
            "Matched Skills",
            len(result["matched"])
        )

    with col3:

        st.metric(
            "Missing Skills",
            len(result["missing"])
        )


    skill_col1, skill_col2, skill_col3 = st.columns(3)


    with skill_col1:

        st.subheader("✅ Matched")

        for skill in result["matched"]:

            st.success(skill)


    with skill_col2:

        st.subheader("❌ Missing")

        for skill in result["missing"]:

            st.error(skill)


    with skill_col3:

        st.subheader("➕ Additional")

        for skill in result["extra"]:

            st.info(skill)


    # ========================================================
    # MODULE 4
    # SKILL GAP ANALYSIS
    # ========================================================

    st.divider()

    st.header(
        "📚 Module 4 — Skill Gap Analysis"
    )


    if not gaps:

        st.success(
            "🎉 No major skill gaps detected!"
        )

    else:

        for gap in gaps:

            st.markdown(
                f"### ❌ {gap['skill']}"
            )

            gap_col1, gap_col2 = st.columns(2)

            with gap_col1:

                st.write(
                    f"**Category:** {gap['category']}"
                )

                st.write(
                    f"**Priority:** {gap['priority']}"
                )

            with gap_col2:

                st.write(
                    "**Recommendation:**"
                )

                st.info(
                    gap["recommendation"]
                )


    # ========================================================
    # MODULE 5
    # ATS SCORING
    # ========================================================

    st.divider()

    st.header(
        "📊 Module 5 — ATS Style Scoring"
    )


    final_score = ats_scores[
        "final_ats_score"
    ]


    score_col1, score_col2 = st.columns(2)

    with score_col1:

        st.metric(
            "FINAL ATS SCORE",
            f"{final_score}/100"
        )

    with score_col2:

        st.progress(
            min(
                max(
                    final_score / 100,
                    0.0
                ),
                1.0
            )
        )


    st.subheader(
        "📈 ATS Score Breakdown"
    )


    ats_col1, ats_col2, ats_col3 = st.columns(3)


    with ats_col1:

        st.metric(
            "Skill Match",
            f"{ats_scores['skill_score']}%"
        )

        st.metric(
            "Keywords",
            f"{ats_scores['keyword_score']}%"
        )


    with ats_col2:

        st.metric(
            "Education",
            f"{ats_scores['education_score']}%"
        )

        st.metric(
            "Projects",
            f"{ats_scores['project_score']}%"
        )


    with ats_col3:

        st.metric(
            "Structure",
            f"{ats_scores['structure_score']}%"
        )

        st.metric(
            "Completeness",
            f"{ats_scores['completeness_score']}%"
        )


    st.subheader(
        "💡 ATS Recommendations"
    )

    for recommendation in ats_recommendations:

        st.write(
            f"• {recommendation}"
        )


    # ========================================================
    # MODULE 6
    # AI GENERATION - SEPARATE BUTTON
    # ========================================================

    st.divider()

    st.header(
        "🤖 Module 6 — AI Generation"
    )

    st.write(
        "AI generation is separate from ATS analysis so "
        "your application remains fast."
    )


    generate_ai_button = st.button(
        "🤖 Generate AI Resume Content",
        use_container_width=True
    )


    if generate_ai_button:

        try:

            with st.spinner(
                "Gemini is generating personalized content..."
            ):

                ai_generator = AIGenerator()

                ai_result = (
                    ai_generator.generate_complete_ai_analysis(

                        name=str(
                            st.session_state[
                                "student"
                            ]["name"]
                        ),

                        target_job=str(
                            st.session_state[
                                "job"
                            ]["job_title"]
                        ),

                        skills=st.session_state[
                            "student_skills"
                        ],

                        missing_skills=st.session_state[
                            "match_result"
                        ]["missing"],

                        education=st.session_state[
                            "resume"
                        ]["education"],

                        projects=st.session_state[
                            "resume"
                        ]["projects"],

                        ats_scores=st.session_state[
                            "ats_scores"
                        ]
                    )
                )


                st.session_state[
                    "ai_result"
                ] = ai_result


            st.success(
                "✅ AI content generated!"
            )


        except Exception as e:

            st.error(
                "❌ AI generation failed."
            )

            st.exception(e)


    # ========================================================
    # DISPLAY AI RESULTS
    # ========================================================

    if "ai_result" in st.session_state:

        ai_result = st.session_state[
            "ai_result"
        ]


        # ====================================================
        # AI STATUS
        # ====================================================

        if ai_result.get(
            "ai_used",
            False
        ):

            st.success(
                "✨ Gemini AI was used."
            )

        else:

            st.info(
                "ℹ️ Gemini was unavailable. "
                "Rule-based fallback was used."
            )


        # ====================================================
        # PROFESSIONAL SUMMARY
        # ====================================================

        st.subheader(
            "📝 Professional Summary"
        )

        st.write(
            ai_result.get(
                "professional_summary",
                ""
            )
        )


        # ====================================================
        # SKILL RECOMMENDATIONS
        # ====================================================

        st.subheader(
            "🎯 AI Skill Recommendations"
        )

        recommendations = ai_result.get(
            "skill_recommendations",
            []
        )


        if isinstance(
            recommendations,
            str
        ):

            st.write(
                recommendations
            )

        else:

            for recommendation in recommendations:

                st.write(
                    f"• {recommendation}"
                )


        # ====================================================
        # PROJECT IMPROVEMENTS
        # ====================================================

        st.subheader(
            "🚀 AI Project Improvements"
        )

        improvements = ai_result.get(
            "project_improvements",
            []
        )


        for project in improvements:

            if isinstance(
                project,
                dict
            ):

                st.markdown(
                    f"### {project.get('name', 'Project')}"
                )

                st.write(
                    project.get(
                        "improved_description",
                        ""
                    )
                )

            else:

                st.write(
                    f"• {project}"
                )


        # ====================================================
        # RESUME IMPROVEMENTS
        # ====================================================

        st.subheader(
            "📌 AI Resume Improvements"
        )

        resume_improvements = ai_result.get(
            "resume_improvements",
            []
        )


        if isinstance(
            resume_improvements,
            str
        ):

            st.write(
                resume_improvements
            )

        else:

            for improvement in resume_improvements:

                st.write(
                    f"• {improvement}"
                )



# ============================================================
# MODULE 8 — RESUME GENERATION
# ============================================================

st.divider()

st.header("📄 Module 8 — Resume Generation")

if st.session_state.get("analysis_complete", False):

    resume_data = st.session_state["resume"].copy()

    # --------------------------------------------------------
    # USE AI SUMMARY IF AVAILABLE
    # --------------------------------------------------------

    if "ai_result" in st.session_state:

        ai_result = st.session_state["ai_result"]

        ai_summary = ai_result.get(
            "professional_summary",
            ""
        )

        if ai_summary:

            resume_data["summary"] = ai_summary

    # --------------------------------------------------------
    # FALLBACK SUMMARY
    # --------------------------------------------------------

    if not resume_data.get("summary"):

        resume_data["summary"] = (
            "Data Science student with hands-on experience "
            "in Python, SQL, Power BI, Excel, Pandas and "
            "data analysis. Interested in applying analytical "
            "and problem-solving skills to real-world "
            "business challenges."
        )

    st.subheader("Resume Preview")

    st.write(
        f"**Name:** {resume_data.get('name', '')}"
    )

    st.write(
        f"**Email:** {resume_data.get('email', '')}"
    )

    st.write(
        f"**Phone:** {resume_data.get('phone', '')}"
    )

    st.write("### Professional Summary")

    st.info(
        resume_data.get(
            "summary",
            ""
        )
    )

    # --------------------------------------------------------
    # GENERATE FILES
    # --------------------------------------------------------

    if st.button(
        "📄 Generate Resume Files",
        type="primary",
        use_container_width=True
    ):

        try:

            import os

            os.makedirs(
                "outputs",
                exist_ok=True
            )

            # =================================================
            # DOCX
            # =================================================

            docx_path = (
                "outputs/AI_Resume.docx"
            )

            resume_generator = ResumeGenerator()

            resume_generator.generate(
                resume_data,
                docx_path
            )

            # =================================================
            # PDF
            # =================================================

            pdf_path = (
                "outputs/AI_Resume.pdf"
            )

            pdf_generator = PDFResumeGenerator()

            pdf_generator.generate(
                resume_data,
                pdf_path
            )

            st.success(
                "✅ Resume generated successfully!"
            )

            # =================================================
            # DOWNLOAD BUTTONS
            # =================================================

            col1, col2 = st.columns(2)

            with col1:

                with open(
                    docx_path,
                    "rb"
                ) as file:

                    st.download_button(

                        label="⬇️ Download DOCX",

                        data=file,

                        file_name="AI_Resume.docx",

                        mime=(
                            "application/"
                            "vnd.openxmlformats-officedocument"
                            ".wordprocessingml.document"
                        ),

                        use_container_width=True
                    )

            with col2:

                with open(
                    pdf_path,
                    "rb"
                ) as file:

                    st.download_button(

                        label="⬇️ Download PDF",

                        data=file,

                        file_name="AI_Resume.pdf",

                        mime="application/pdf",

                        use_container_width=True
                    )

        except Exception as e:

            st.error(
                "❌ Resume generation failed."
            )

            st.exception(e)

else:

    st.info(
        "Run Resume Analysis first."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AI Resume & Portfolio Builder | "
    "NLP + Skill Matching + Skill Gap Analysis + "
    "ATS Scoring + Gemini AI"
)