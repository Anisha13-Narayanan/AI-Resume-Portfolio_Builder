# 📄 AI Resume & Portfolio Builder

An AI-powered career assistance application that helps students and job seekers analyze their skills against job requirements, identify skill gaps, calculate an ATS-style resume score, generate AI-powered recommendations, and create professional resumes in DOCX and PDF formats.

---

## 🌐 Project Links

### 💻 GitHub Repository

https://github.com/Anisha13-Narayanan/AI-Resume-Portfolio_Builder

### 🚀 Live Application

https://ai-resume-portfoliobuilder-szj3xszpc8mz62t6gtwoq2.streamlit.app/

---

## 📌 Project Overview

The **AI Resume & Portfolio Builder** is a Python-based application designed to help students and job seekers improve their resumes according to the requirements of a target job.

The system combines:

- Natural Language Processing
- Skill Extraction
- Skill Matching
- Skill Gap Analysis
- ATS-style Resume Scoring
- Generative AI
- Resume Generation
- Streamlit Web Application

The application analyzes the relationship between a student's current skills and the skills required by a selected job.

---

## 🎯 Objectives

The main objectives of this project are:

1. Extract required skills from job descriptions.
2. Compare student skills with job requirements.
3. Identify matched, missing, and additional skills.
4. Analyze skill gaps.
5. Provide personalized learning recommendations.
6. Calculate an ATS-style resume score.
7. Generate AI-powered professional summaries.
8. Recommend additional skills.
9. Suggest project improvements.
10. Generate professional resumes in DOCX and PDF formats.
11. Provide an interactive web interface.
12. Deploy the application as a web application.

---

# ✨ Key Features

## 🔎 1. NLP Skill Extraction

The application automatically extracts relevant skills from job descriptions.

### Example

Input:

    We are looking for a Junior Data Analyst with experience in
    Python, SQL, Power BI, Excel, Pandas and Statistics.

Output:

    Python
    SQL
    Power BI
    Excel
    Pandas
    Statistics

---

## 🎯 2. Skill Matching

The application compares the student's current skills with the requirements of the selected job.

It identifies:

### ✅ Matched Skills

Skills already available in the student's profile.

### ❌ Missing Skills

Skills required by the job but missing from the student's profile.

### ➕ Additional Skills

Skills available in the student's profile that are not directly required by the selected job.

The system also calculates an overall skill-match percentage.

---

## 📚 3. Personalized Skill Gap Analysis

The application analyzes missing skills and provides recommendations.

For each skill gap, the system provides:

- Skill
- Category
- Priority
- Learning Recommendation

### Example

    Missing Skill: Tableau

    Category:
    Data Visualization

    Priority:
    Medium

    Recommendation:
    Learn Tableau fundamentals and demonstrate the skill through a dashboard project.

---

# 📊 4. ATS-Style Resume Scoring

The application calculates an ATS-style resume compatibility score using multiple factors.

| Component | Weight |
|---|---:|
| Skill Match | 40% |
| Keyword Matching | 20% |
| Education | 10% |
| Projects | 15% |
| Resume Structure | 10% |
| Resume Completeness | 5% |
| **Total** | **100%** |

### Score Components

#### Skill Match

Measures the percentage of required skills matched by the student.

#### Keyword Matching

Measures keyword overlap between the resume and target job description.

#### Education

Checks:

- Degree
- Field
- Institution
- Graduation year

#### Projects

Evaluates:

- Number of projects
- Project name
- Project description
- Technologies used

#### Resume Structure

Checks important sections such as:

- Summary
- Skills
- Education
- Projects
- Experience

#### Resume Completeness

Checks whether important personal and resume information is available.

---

## 📈 Example ATS Result

    ======================================================================
    MODULE 5 - ATS STYLE SCORING
    ======================================================================

    ATS SCORE BREAKDOWN
    ----------------------------------------------------------------------

    Skill Match Score    : 75.0%
    Keyword Score        : 77.78%
    Education Score      : 100%
    Project Score        : 100.0%
    Structure Score      : 80.0%
    Completeness Score   : 100.0%

    ----------------------------------------------------------------------

    FINAL ATS SCORE      : 83.56/100

    RECOMMENDATIONS
    ----------------------------------------------------------------------

    • Resume has strong ATS compatibility.

---

# 🤖 5. Gemini AI Integration

The application integrates Google Gemini for AI-powered resume analysis and content generation.

Gemini is used for:

- Professional Summary Generation
- Skill Recommendations
- Project Improvement Suggestions
- Resume Improvement Recommendations

### Example AI Professional Summary

    BSc Data Science with hands-on experience in Python, SQL,
    Power BI, Excel, Pandas and Statistics. Developed relevant
    data analysis projects and seeking a Junior Data Analyst role.

### Example Skill Recommendations

    • Consider learning or demonstrating Tableau if relevant.
    • Consider learning or demonstrating Machine Learning if relevant.

### Example Project Improvements

    • Highlight measurable results.
    • Explain technical contributions.
    • Mention technologies used.
    • Describe the business problem solved.

---

# 🛡️ Gemini AI Fallback System

The application contains a rule-based fallback mechanism.

If Gemini is unavailable because of:

- API quota limits
- Rate limits
- Temporary service errors
- Model availability issues
- Network problems

the application continues using rule-based recommendations.

Example:

    Gemini request failed.
    Using rule-based fallback.

This ensures that the core application remains functional even when the AI service is temporarily unavailable.

---

# 📄 6. Resume Generation

The application generates professional resumes containing:

- Personal Information
- Professional Summary
- Skills
- Education
- Projects
- Experience
- Job-targeted Recommendations

Supported formats:

    DOCX
    PDF

---

# 🖥️ 7. Streamlit Web Application

The entire project is integrated into an interactive Streamlit application.

The user can:

1. Select a student.
2. Select a target job.
3. Extract required skills.
4. Analyze skill matching.
5. View skill gaps.
6. Calculate ATS score.
7. Generate AI recommendations.
8. Generate a resume.
9. Download the generated resume.

---

# 🔄 Application Workflow

    ┌─────────────────────┐
    │      CSV DATA       │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │     DATA LOADER     │
    └──────────┬──────────┘
               │
       ┌───────┴────────┐
       ▼                ▼
    ┌───────────────┐  ┌──────────────────┐
    │Student Profile│  │ Job Description  │
    └───────┬───────┘  └────────┬─────────┘
            │                   │
            │                   ▼
            │        ┌─────────────────────┐
            │        │ NLP Skill Extraction│
            │        └──────────┬──────────┘
            │                   │
            └─────────┬─────────┘
                      ▼
            ┌─────────────────────┐
            │   Skill Matching    │
            └──────────┬──────────┘
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
          Matched   Missing   Additional
           Skills    Skills     Skills
                       │
                       ▼
            ┌─────────────────────┐
            │ Skill Gap Analysis  │
            └──────────┬──────────┘
                       │
                       ▼
            ┌─────────────────────┐
            │    ATS Scoring      │
            └──────────┬──────────┘
                       │
              ┌────────┴─────────┐
              ▼                  ▼
       ┌──────────────┐   ┌──────────────────┐
       │  Gemini AI   │   │Resume Generation │
       │Recommendations│  │    DOCX / PDF    │
       └──────────────┘   └──────────────────┘

---

# 🏗️ Project Structure

    AI-Resume-Portfolio_Builder/
    │
    ├── app.py
    ├── requirements.txt
    ├── README.md
    ├── .gitignore
    │
    ├── data/
    │   └── raw/
    │       ├── students.csv
    │       ├── jobs.csv
    │       ├── job_descriptions.csv
    │       ├── skills.csv
    │       ├── skill_categories.csv
    │       └── skill_matching.csv
    │
    ├── src/
    │   ├── __init__.py
    │   │
    │   ├── data/
    │   │   ├── __init__.py
    │   │   └── data_loader.py
    │   │
    │   ├── nlp/
    │   │   ├── __init__.py
    │   │   └── skill_extractor.py
    │   │
    │   ├── analysis/
    │   │   ├── __init__.py
    │   │   ├── skill_matcher.py
    │   │   ├── skill_gap_analyzer.py
    │   │   ├── ats_scorer.py
    │   │   └── ai_generator.py
    │   │
    │   └── documents/
    │       ├── __init__.py
    │       ├── resume_generator.py
    │       └── pdf_generator.py
    │
    └── outputs/

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Scikit-learn | Data Analysis / ML Utilities |
| spaCy | Natural Language Processing |
| Streamlit | Web Application |
| Plotly | Data Visualization |
| Google Gemini | Generative AI |
| google-genai | Gemini API Integration |
| python-docx | DOCX Generation |
| ReportLab | PDF Generation |
| pypdf | PDF Processing |
| python-dotenv | Environment Variables |
| Git | Version Control |
| GitHub | Source Code Hosting |

---

# 📦 Installation

## 1. Clone the Repository

    git clone https://github.com/Anisha13-Narayanan/AI-Resume-Portfolio_Builder.git

Navigate to the project:

    cd AI-Resume-Portfolio_Builder

---

# 2. Create a Virtual Environment

Windows:

    python -m venv .venv

Activate:

    .venv\Scripts\activate

---

# 3. Install Dependencies

    pip install -r requirements.txt

---

# 📋 Requirements

The project uses the following Python packages:

    pandas
    numpy
    scikit-learn
    spacy
    streamlit
    plotly
    reportlab
    python-docx
    python-dotenv
    pypdf
    google-genai

---

# 🔐 Gemini API Configuration

The Gemini API key is loaded using an environment variable.

## Local Development

Create a `.env` file in the project root:

    GEMINI_API_KEY=your_api_key_here

The application reads the key using:

    import os
    from dotenv import load_dotenv

    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

---

# 🔒 Security

API keys should never be hardcoded in Python files.

Do not commit:

    .env
    .streamlit/secrets.toml

Your `.gitignore` should include:

    .venv/
    __pycache__/
    .env
    .streamlit/secrets.toml
    outputs/
    *.pyc

For cloud deployment, configure the Gemini API key through the platform's secret-management system.

---

# ▶️ Run the Application Locally

Activate the virtual environment:

    .venv\Scripts\activate

Run Streamlit:

    streamlit run app.py

The application will open in your browser.

---

# 🧪 Testing

## Skill Matching Test

    python -m src.analysis.test_skill_matcher

---

## ATS Scoring Test

    python -m src.analysis.test_ats_scorer

---

## Gemini AI Test

    python -m src.analysis.test_gemini_ai

If Gemini reaches its API quota, the application uses the rule-based fallback system.

---

# 📊 Project Modules

| Module | Description | Status |
|---|---|---|
| Module 1 | Project Setup & Data Loading | ✅ Completed |
| Module 2 | NLP Skill Extraction | ✅ Completed |
| Module 3 | Skill Matching | ✅ Completed |
| Module 4 | Skill Gap Analysis | ✅ Completed |
| Module 5 | ATS-Style Scoring | ✅ Completed |
| Module 6 | Gemini AI Generation | ✅ Completed |
| Module 7 | Streamlit UI | ✅ Completed |
| Module 8 | Resume Generation | ✅ Completed |
| Module 9 | GitHub Integration | ✅ Completed |
| Module 10 | Cloud Deployment | 🔄 In Progress |

---

# 📈 Example End-to-End Analysis

    Student:
    Data Science Student

    Target Job:
    Junior Data Analyst

    Current Skills:
    Python
    SQL
    Power BI
    Excel
    Pandas
    Statistics

    Matched Skills:
    Python
    SQL
    Power BI
    Excel
    Pandas
    Statistics

    Missing Skills:
    Tableau
    Machine Learning

    Skill Match:
    75%

    ATS Score:
    83.56 / 100

    AI Recommendations:
    • Consider learning Tableau.
    • Consider demonstrating Machine Learning.
    • Improve project descriptions.
    • Highlight measurable results.

---

# 🎓 Target Users

The application is designed primarily for:

- Data Science Students
- Data Analytics Students
- Fresh Graduates
- Job Seekers
- College Placement Cells
- Career Development Programs

---

# 💡 Use Cases

## Student Career Preparation

Helps students understand whether their current skills match a target job.

## Resume Optimization

Identifies missing skills and important job-related keywords.

## Skill Development

Provides recommendations for closing skill gaps.

## Job Matching

Allows users to compare their skills against different job roles.

## Resume Generation

Creates a professional resume based on the student's profile and target job.

---

# 🚀 Deployment

The application is designed to run as a cloud-based Streamlit application.

Deployment workflow:

    GitHub Repository
            ↓
    Streamlit Community Cloud
            ↓
    Configure Application
            ↓
    Configure Gemini Secret
            ↓
    Install requirements.txt
            ↓
    Run app.py
            ↓
    Public Web Application

The Gemini API key should be added through Streamlit Secrets and should never be committed to GitHub.


---

# 🏆 Project Highlights

This project demonstrates practical knowledge of:

- Python
- Data Processing
- Natural Language Processing
- Skill Extraction
- Skill Matching
- Recommendation Systems
- ATS-style Scoring
- Generative AI
- API Integration
- Streamlit
- Document Generation
- Git
- GitHub
- Cloud Deployment

---

# 🔮 Future Improvements

Future versions may include:

- Job Recommendation System
- Advanced Semantic Skill Matching
- Resume Template Selection
- Cover Letter Generation
- LinkedIn Profile Optimization
- Portfolio Website Generation
- Personalized Learning Roadmap
- Job Description Comparison
- Resume History
- User Authentication
- Database Integration
- Advanced Resume Analytics
- Improved AI Personalization

---

# 👩‍💻 Author

**Anisha.N**

Postgraduate Diploma in Data Science and Analytics

---

# 📜 License

This project is developed for educational, academic, and portfolio purposes.

---

# ⭐ Conclusion

The **AI Resume & Portfolio Builder** combines NLP, data analysis, skill matching, skill-gap analysis, ATS-style scoring, Generative AI, and document generation into a single practical application.

The system helps students and job seekers:

- Understand their job readiness
- Identify missing skills
- Improve their resume
- Receive personalized recommendations
- Generate professional resumes
- Prepare for target job roles

The project demonstrates an end-to-end implementation from data processing and analysis to AI integration, web application development, GitHub version control, and cloud deployment.

---

## 🔗 GitHub Repository

https://github.com/Anisha13-Narayanan/AI-Resume-Portfolio_Builder

## 🚀 Live Application

_Add the Streamlit URL here after successful deployment._