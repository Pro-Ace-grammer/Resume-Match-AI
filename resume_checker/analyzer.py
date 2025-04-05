import json
import pdfplumber
import spacy
from groq import Groq


def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()+"\n"

    return text.strip()


API_KEY="Your-Groq-API-Key"


def analyze_resume_with_llm(resume_text:str,job_description:str)->dict:
    prompt = f"""
    You are an AI assisstant that analyzes resumes for software engineering job applications.
    Given a resume and a job description, extract the following details:
    1. identify all skills mentioned in the resume
    2. calculate the total years of experience.
    3. Categories the projects based on the domain (eg AI, Web development, Cloud etc)
    4. Rank the resume relevance to the job description on a scale of 0 to 100. And the ranking should be given after a very strict correction.
    Resume:
    {resume_text}
    Job Description:
    {job_description}

    Provide the output in valid JSON format with this structure.
    {{
        "rank":"<percentage>",
        "skills":["skill1","skill2",...],
        "total_experience":"<number of years>",
        "project_category":["cat1","cat2"...],
        "skills_matching":"<how many no of> skills are matching out of <total technical skills> from Job Description"
    }}
"""
    try:
        client = Groq(api_key=API_KEY)
        response=client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages= [{'role':'user','content':prompt}],
            temperature=0.7,
            response_format={'type':"json_object"}
        )
        result = response.choices[0].message.content
        return json.loads(result)
    except Exception as e:
        print(e)



def process_resume(pdf_path, job_description):
    try:
        resume_text = extract_text_from_pdf(pdf_path)
        data = analyze_resume_with_llm(resume_text,job_description)
        return data
    except Exception as e:
        print(e)
        return None
