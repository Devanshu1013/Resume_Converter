Resume Parser and PDF Generator
This Python script allows users to upload their resume in PDF format, extract relevant information such as name, skills, experience, education, projects, hackathons, and achievements, and then generate a professional resume in PDF format.

Features
Resume Parsing: Extracts text from the uploaded PDF resume using PyPDF2.
Information Extraction: Utilizes regular expressions to extract name, skills, experience, education, projects, hackathons, and achievements from the resume text.
PDF Generation: Creates a professional resume in PDF format using ReportLab library, incorporating the extracted information.
Streamlit Interface: Provides a user-friendly interface using Streamlit for uploading the resume and generating the PDF.
How to Use
Install the required Python packages by running pip install -r requirements.txt.
Run the script by executing streamlit run resume_parser.py in your terminal.
Upload your resume in PDF format using the provided file uploader.
Once the resume is uploaded, the script extracts relevant information and displays it on the Streamlit interface.
Click the "Generate PDF" button to create and download the professional resume in PDF format.
Requirements
Python 3.x
PyPDF2
ReportLab
Streamlit
Usage
arduino
Copy code
streamlit run resume_parser.py
Contributors
Your Name
