# 📄 AI Resume & Portfolio Builder

An AI-powered web application that helps students and job seekers analyze their skills against job requirements, identify skill gaps, calculate an ATS-style resume score, generate AI-powered resume recommendations, and create professional resumes in DOCX and PDF formats.

---

## 📌 Project Overview

The **AI Resume & Portfolio Builder** is a career-assistance application developed using Python, NLP, data analysis, Generative AI, and Streamlit.

The application allows a user to:

1. Select a student profile.
2. Select a target job.
3. Extract required skills from the job description.
4. Compare student skills with job requirements.
5. Identify matched and missing skills.
6. Analyze skill gaps.
7. Calculate an ATS-style resume score.
8. Generate AI-powered resume recommendations.
9. Generate professional resume documents.
10. Download the generated resume in DOCX and PDF formats.

The goal is to help students understand their readiness for a target job and improve their resume based on actual job requirements.

---

# 🎯 Objectives

The main objectives of this project are:

- Automatically extract skills from job descriptions.
- Match student skills with job requirements.
- Identify missing and additional skills.
- Provide personalized skill-gap recommendations.
- Calculate an ATS-style resume compatibility score.
- Generate professional resume summaries using Generative AI.
- Suggest relevant skills to learn.
- Suggest improvements for projects.
- Provide resume improvement recommendations.
- Generate professional resumes in DOCX and PDF formats.
- Provide an easy-to-use Streamlit web interface.

---

# ✨ Key Features

## 🔎 1. NLP Skill Extraction

The application extracts relevant technical and professional skills from job descriptions.

### Example

Input:

```text
We are looking for a Junior Data Analyst with experience in
Python, SQL, Power BI, Excel, Pandas and Statistics.

Output:

Python
SQL
Power BI
Excel
Pandas
Statistics

This allows the system to identify the skills required for a specific job.

🎯 2. Skill Matching

The system compares the student's current skills with the skills extracted from the target job.

The application identifies:

✅ Matched Skills

Skills the student already has.

❌ Missing Skills

Skills required by the job but not currently available in the student's profile.

➕ Additional Skills

Skills the student has that are not directly required by the selected job.

The system also calculates an overall skill-match percentage.

📚 3. Personalized Skill Gap Analysis

The skill-gap module analyzes missing skills and provides personalized recommendations.

For each missing skill, the system provides:

Skill name
Skill category
Priority
Learning recommendation
Example
Missing Skill: Tableau

Category:
Data Visualization

Priority:
Medium

Recommendation:
Learn Tableau fundamentals and create a dashboard project.

This helps students identify what they should learn to improve their job readiness.

📊 4. ATS-Style Resume Scoring

The application calculates an ATS-style resume score using multiple factors.

The scoring system contains:

Component	Weight
Skill Match	40%
Keyword Matching	20%
Education	10%
Projects	15%
Resume Structure	10%
Resume Completeness	5%
Total	100%
ATS Score Components
Skill Match Score

Measures how many required job skills are present in the student's skills.

Keyword Score

Measures keyword overlap between the resume and job description.

Education Score

Checks the completeness of:

Degree
Field
Institution
Graduation year
Project Score

Evaluates:

Number of projects
Project name
Project description
Technologies used
Structure Score

Checks important resume sections such as:

Summary
Skills
Education
Projects
Experience
Completeness Score

Checks whether important personal and resume information is available.

Checks whether important personal and resume information is available.

📈 Example ATS Result

Example output:

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
🤖 5. Gemini AI Integration

The application integrates Google Gemini for Generative AI functionality.

Gemini can generate:

Professional summaries
Skill recommendations
Project improvement suggestions
Resume improvement recommendations
AI Professional Summary

Example:

BSc Data Science with hands-on experience in Python, SQL,
Power BI, Excel, Pandas and Statistics. Developed relevant
data analysis projects and seeking a Junior Data Analyst role.
AI Skill Recommendations

The system can recommend additional skills based on the target role.

Example:

• Consider learning or demonstrating Tableau if relevant.
• Consider learning or demonstrating Machine Learning if relevant.
AI Project Improvements

The system can recommend how to improve project descriptions by:

Highlighting technical contributions
Adding measurable results
Mentioning technologies
Explaining the business problem solved
🛡️ Gemini Fallback System

The application includes a rule-based fallback mechanism.

If Gemini is temporarily unavailable because of:

API quota limits
Rate limits
Temporary service errors
Model availability issues
Network problems

the application continues working using predefined rule-based recommendations.

Therefore, Gemini availability is not required for the core application to function.

Example:

Gemini request failed.
Using rule-based fallback.
📄 6. Resume Generation

The application generates professional resumes from the analyzed student information.

Supported formats:

DOCX
PDF

The generated resume can contain:

Personal Information
        ↓
Professional Summary
        ↓
Technical Skills
        ↓
Education
        ↓
Projects
        ↓
Experience
🖥️ 7. Streamlit Web Application

The complete system is integrated into a Streamlit interface.

The application provides an interactive workflow for:

Student selection
Job selection
Skill extraction
Skill matching
Skill-gap analysis
ATS scoring
AI recommendations
Resume generation
🔄 Application Workflow
                    ┌─────────────────────┐
                    │      CSV DATA       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     DATA LOADER     │
                    └──────────┬──────────┘
                               │
              ┌────────────────┴────────────────┐
              │                                 │
              ▼                                 ▼
    ┌────────────────────┐           ┌────────────────────┐
    │ Student Profile    │           │ Job Description    │
    └──────────┬─────────┘           └──────────┬─────────┘
               │                                │
               │                                ▼
               │                     ┌────────────────────┐
               │                     │ NLP Skill          │
               │                     │ Extraction         │
               │                     └──────────┬─────────┘
               │                                │
               └────────────────┬───────────────┘
                                ▼
                    ┌─────────────────────┐
                    │   SKILL MATCHING    │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
             Matched        Missing        Extra
              Skills         Skills        Skills
                               │
                               ▼
                    ┌─────────────────────┐
                    │  SKILL GAP ANALYSIS │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   ATS SCORING       │
                    └──────────┬──────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
       ┌─────────────────┐          ┌────────────────────┐
       │   GEMINI AI     │          │ RESUME GENERATION  │
       │ Recommendations │          │ DOCX / PDF         │
       └─────────────────┘          └────────────────────┘
🏗️ Project Structure
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
🛠️ Technologies Used
Programming Language
Python 3.x
Data Processing
Pandas
NumPy
Machine Learning / NLP
Scikit-learn
spaCy
NLP-based skill extraction
Generative AI
Google Gemini API
Google GenAI SDK
Web Application
Streamlit
Visualization
Plotly
Document Generation
python-docx
ReportLab
pypdf
Environment Management
python-dotenv
Python Virtual Environment
Version Control
Git
GitHub
📦 Installation
1. Clone the Repository
git clone https://github.com/Anisha13-Narayanan/AI-Resume-Portfolio_Builder.git

Move into the project directory:

cd AI-Resume-Portfolio_Builder
2. Create a Virtual Environment

Windows:

python -m venv .venv

Activate the environment:

.venv\Scripts\activate
3. Install Dependencies

Install all required packages:

pip install -r requirements.txt
📋 Requirements

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
🔐 Gemini API Configuration

The Gemini API key is loaded through an environment variable.

The API key should never be hardcoded into the source code or committed to GitHub.

Local Development

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here

The application loads the key using:

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
🔒 Security

The following files must not be committed to GitHub:

.env
.streamlit/secrets.toml

The .gitignore file should contain:

.venv/
__pycache__/
.env
.streamlit/secrets.toml
outputs/
*.pyc

Never publish:

Gemini API keys
Passwords
Authentication tokens
Private credentials
▶️ Running the Application

After activating the virtual environment and installing dependencies:

streamlit run app.py

The application will start locally and open in a browser.

🧪 Testing

The individual modules can be tested separately.

Test Skill Matching
python -m src.analysis.test_skill_matcher
Test ATS Scoring
python -m src.analysis.test_ats_scorer
Test Gemini AI
python -m src.analysis.test_gemini_ai

Gemini may occasionally return temporary errors or quota limitations.

The application uses a rule-based fallback when Gemini is unavailable.

📊 Project Modules
Module	Description	Status
Module 1	Project Setup & Data Loading	✅ Completed
Module 2	NLP Skill Extraction	✅ Completed
Module 3	Skill Matching	✅ Completed
Module 4	Skill Gap Analysis	✅ Completed
Module 5	ATS-Style Scoring	✅ Completed
Module 6	AI Resume Generation	✅ Completed
Module 7	Streamlit UI	✅ Completed
Module 8	Resume / Portfolio Generation	✅ Completed
Module 9	Testing & Deployment	🔄 In Progress
📈 Example Application Output

A typical analysis can produce:

Student:
Data Science Student

Target Job:
Junior Data Analyst

Skill Match:
75%

Matched Skills:
Python
SQL
Excel
Power BI
Pandas

Missing Skills:
Tableau
Machine Learning

ATS Score:
83.56 / 100

AI Recommendations:
Improve project descriptions
Add measurable results
Consider learning Tableau
Consider demonstrating Machine Learning
🎓 Target Users

This application is primarily designed for:

Data Science students
Data Analytics students
Fresh graduates
Job seekers
Career development programs
College placement cells
💡 Use Cases
Student Career Preparation

Students can identify which skills they need for a particular job.

Resume Optimization

Students can identify missing keywords and improve resume structure.

Job Matching

Users can compare their current skills with multiple job descriptions.

Skill Development

The application provides recommendations for closing skill gaps.

Resume Generation

Users can generate a professional resume based on their profile and target role.

🚀 Future Improvements

The following features can be added in future versions:

Job recommendation system
Advanced semantic skill matching
Resume template selection
Cover letter generation
LinkedIn profile optimization
Portfolio website generation
Job description comparison
Personalized learning roadmap
Resume history
User authentication
Database integration
Cloud deployment
Improved AI personalization
Interactive analytics dashboard
🌐 Deployment

The application is designed to be deployed as a Streamlit web application.

Deployment steps include:

GitHub Repository
        ↓
Streamlit Community Cloud
        ↓
Configure Secrets
        ↓
Install requirements.txt
        ↓
Deploy app.py
        ↓
Public Web Application

The Gemini API key should be configured through the deployment platform's secret management system rather than being stored in the GitHub repository.

📌 Current Project Status
Project Setup                  ✅
Dataset Loading                ✅
NLP Skill Extraction           ✅
Skill Matching                 ✅
Skill Gap Analysis             ✅
ATS-Style Scoring              ✅
Gemini AI Integration          ✅
AI Fallback System             ✅
Streamlit Application          ✅
DOCX Resume Generation         ✅
PDF Resume Generation          ✅
GitHub Integration             ✅
Testing                        🔄
Cloud Deployment               🔄
Portfolio Generation           🔄
🏆 Project Highlights

This project demonstrates practical implementation of:

Python programming
Data processing
Natural Language Processing
Skill extraction
Recommendation systems
ATS-style scoring
Generative AI
API integration
Streamlit development
Document generation
Git and GitHub
Application deployment
👩‍💻 Author

Anisha N
Data Science

📜 License

This project is intended for educational and portfolio purposes.

⭐ Conclusion

The AI Resume & Portfolio Builder combines NLP, data analysis, skill matching, skill-gap analysis, ATS-style scoring, Generative AI, and document generation into one practical application.

The system helps students and job seekers understand their suitability for a target job, identify areas for improvement, receive personalized recommendations, and generate a professional resume.

🔗 Repository

GitHub:

https://github.com/Anisha13-Narayanan/AI-Resume-Portfolio_Builder