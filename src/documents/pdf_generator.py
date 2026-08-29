from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch


class PDFResumeGenerator:

    def __init__(self):

        self.styles = getSampleStyleSheet()

        self.name_style = ParagraphStyle(
            "ResumeName",
            parent=self.styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=20,
            alignment=TA_CENTER,
            spaceAfter=4
        )

        self.contact_style = ParagraphStyle(
            "Contact",
            parent=self.styles["Normal"],
            fontName="Helvetica",
            fontSize=9,
            alignment=TA_CENTER,
            spaceAfter=8
        )

        self.heading_style = ParagraphStyle(
            "SectionHeading",
            parent=self.styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11,
            spaceBefore=8,
            spaceAfter=4
        )

        self.body_style = ParagraphStyle(
            "Body",
            parent=self.styles["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=13,
            spaceAfter=4
        )

        self.project_style = ParagraphStyle(
            "Project",
            parent=self.styles["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=13,
            spaceAfter=2
        )

    # ---------------------------------------------------------
    # ADD SECTION
    # ---------------------------------------------------------

    def add_section_heading(self, story, title):

        story.append(
            Paragraph(
                title.upper(),
                self.heading_style
            )
        )

        story.append(
            HRFlowable(
                width="100%",
                thickness=0.6,
                spaceAfter=5
            )
        )

    # ---------------------------------------------------------
    # GENERATE PDF
    # ---------------------------------------------------------

    def generate(self, resume, output_path):

        document = SimpleDocTemplate(

            output_path,

            pagesize=A4,

            rightMargin=0.55 * inch,
            leftMargin=0.55 * inch,
            topMargin=0.5 * inch,
            bottomMargin=0.5 * inch
        )

        story = []

        # =====================================================
        # HEADER
        # =====================================================

        name = resume.get(
            "name",
            ""
        )

        email = resume.get(
            "email",
            ""
        )

        phone = resume.get(
            "phone",
            ""
        )

        story.append(
            Paragraph(
                name,
                self.name_style
            )
        )

        contact = []

        if email:
            contact.append(email)

        if phone:
            contact.append(phone)

        if contact:

            story.append(
                Paragraph(
                    " | ".join(contact),
                    self.contact_style
                )
            )

        # =====================================================
        # SUMMARY
        # =====================================================

        summary = resume.get(
            "summary",
            ""
        )

        if summary:

            self.add_section_heading(
                story,
                "Professional Summary"
            )

            story.append(
                Paragraph(
                    summary,
                    self.body_style
                )
            )

        # =====================================================
        # SKILLS
        # =====================================================

        skills = resume.get(
            "skills",
            []
        )

        if skills:

            self.add_section_heading(
                story,
                "Technical Skills"
            )

            if isinstance(skills, list):

                skill_text = " • ".join(
                    str(skill)
                    for skill in skills
                )

            else:

                skill_text = str(skills)

            story.append(
                Paragraph(
                    skill_text,
                    self.body_style
                )
            )

        # =====================================================
        # EDUCATION
        # =====================================================

        education = resume.get(
            "education",
            {}
        )

        if education:

            self.add_section_heading(
                story,
                "Education"
            )

            degree = education.get(
                "degree",
                ""
            )

            field = education.get(
                "field",
                ""
            )

            institution = education.get(
                "institution",
                ""
            )

            year = education.get(
                "graduation_year",
                ""
            )

            education_text = ""

            if degree:
                education_text += (
                    f"<b>{degree}</b>"
                )

            if field:
                education_text += (
                    f" — {field}"
                )

            if institution:
                education_text += (
                    f"<br/>{institution}"
                )

            if year:
                education_text += (
                    f" | {year}"
                )

            story.append(
                Paragraph(
                    education_text,
                    self.body_style
                )
            )

        # =====================================================
        # PROJECTS
        # =====================================================

        projects = resume.get(
            "projects",
            []
        )

        if projects:

            self.add_section_heading(
                story,
                "Projects"
            )

            for project in projects:

                name = project.get(
                    "name",
                    ""
                )

                description = project.get(
                    "description",
                    ""
                )

                technologies = project.get(
                    "technologies",
                    []
                )

                if isinstance(
                    technologies,
                    list
                ):

                    tech_text = ", ".join(
                        str(x)
                        for x in technologies
                    )

                else:

                    tech_text = str(
                        technologies
                    )

                project_text = ""

                if name:

                    project_text += (
                        f"<b>{name}</b>"
                    )

                if tech_text:

                    project_text += (
                        f" | {tech_text}"
                    )

                if description:

                    project_text += (
                        f"<br/>{description}"
                    )

                story.append(
                    Paragraph(
                        project_text,
                        self.project_style
                    )
                )

                story.append(
                    Spacer(
                        1,
                        4
                    )
                )

        # =====================================================
        # EXPERIENCE
        # =====================================================

        experience = resume.get(
            "experience",
            ""
        )

        if experience:

            self.add_section_heading(
                story,
                "Experience"
            )

            story.append(
                Paragraph(
                    experience,
                    self.body_style
                )
            )

        # =====================================================
        # BUILD
        # =====================================================

        document.build(story)

        return output_path