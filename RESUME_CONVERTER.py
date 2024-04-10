import streamlit as st
import re
import tempfile
from PyPDF2 import PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def extract_text_from_pdf(uploaded_file):
    text = ""
    try:
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            text += page.extract_text()
    except Exception as e:
        st.error("Error reading PDF file:", e)
    return text


def extract_name(text):
    name = re.search(r'^[^\n]+', text).group()
    return name

def extract_skills(text):
    skills_pattern = re.compile(r'(?:skills|technologies|tools):?\s*(.*?)(?:experience|education|projects|hackathons|achievements|$)', re.IGNORECASE | re.DOTALL)
    skills_match = skills_pattern.search(text)
    if skills_match:
        return skills_match.group(1)
    else:
        return ""

def extract_experience(text):
    experience_pattern = re.compile(r'experience:?\s*(.*?)(?:education|projects|hackathons|achievements|$)', re.IGNORECASE | re.DOTALL)
    experience_match = experience_pattern.search(text)
    if experience_match:
        return experience_match.group(1)
    else:
        return ""

def extract_education(text):
    education_pattern = re.compile(r'education:?\s*(.*?)(?:projects|hackathons|achievements|$)', re.IGNORECASE | re.DOTALL)
    education_match = education_pattern.search(text)
    if education_match:
        return education_match.group(1)
    else:
        return ""

def extract_projects(text):
    projects_pattern = re.compile(r'projects:?\s*(.*?)(?:hackathons|achievements|Skills|$)', re.IGNORECASE | re.DOTALL)
    projects_match = projects_pattern.search(text)
    if projects_match:
        return projects_match.group(1)
    else:
        return ""

def extract_hackathons(text):
    hackathons_pattern = re.compile(r'hackathons:?\s*(.*?)(?:achievements|$)', re.IGNORECASE | re.DOTALL)
    hackathons_match = hackathons_pattern.search(text)
    if hackathons_match:
        return hackathons_match.group(1)
    else:
        return ""
    
def extract_achievements(text):
    achievements_pattern = re.compile(r'achievements:?\s*(.*?)(?:education|projects|hackathons|Work|Languages|$)', re.IGNORECASE | re.DOTALL)
    achievements_match = achievements_pattern.search(text)
    if achievements_match:
        return achievements_match.group(1)
    else:
        return ""

def create_resume_pdf(name, skills, experience, achievements, education, hackathons, projects, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()

    title = "Professional Resume"
    content = [Paragraph(title, styles['Title']), Spacer(1, 12)]

    content.append(Paragraph("Name:", styles['Heading2']))
    content.append(Paragraph(name, styles['Normal']))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Skills:", styles['Heading2']))
    content.append(Paragraph(skills, styles['Normal']))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Experience:", styles['Heading2']))
    content.append(Paragraph(experience, styles['Normal']))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Achievements:", styles['Heading2']))
    content.append(Paragraph(achievements, styles['Normal']))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Education:", styles['Heading2']))
    content.append(Paragraph(education, styles['Normal']))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Hackathons:", styles['Heading2']))
    content.append(Paragraph(hackathons, styles['Normal']))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Projects:", styles['Heading2']))
    content.append(Paragraph(projects, styles['Normal']))
    content.append(Spacer(1, 12))

    doc.build(content)

# Streamlit frontend
st.title("Resume Parser and PDF Generator")

uploaded_file = st.file_uploader("Upload your resume (PDF format)", type="pdf")

if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    name = extract_name(resume_text)
    skills = extract_skills(resume_text)
    experience = extract_experience(resume_text)
    education = extract_education(resume_text)
    projects = extract_projects(resume_text)
    hackathons = extract_hackathons(resume_text)
    achievements = extract_achievements(resume_text)

    st.write(" ")
    st.write(f"**Resume of:** {name} ")
    st.write(" ")
    st.write(f"**Name:** {name}")
    st.write(f"**Skills:** {skills}")
    st.write(f"**Experience:** {experience}")
    st.write(f"**Achievements:** {achievements}")
    st.write(f"**Education:** {education}")
    st.write(f"**Hackathons:** {hackathons}")
    st.write(f"**Projects:** {projects}")
    st.write(" ")

    if st.button("Generate PDF"):
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            create_resume_pdf(name, skills, experience, achievements, education, hackathons, projects, tmp_file.name)
            st.write(" ")
            st.write("Click below to download the PDF:")
            st.download_button(
                label="Download PDF",
                data=tmp_file.name,
                file_name=f"{name}_resume.pdf",
                mime="application/pdf"
            )