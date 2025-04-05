# 🧠 Resume Match AI (LLM + Django)

An intelligent resume ranking and analysis web application built with **Django**, **REST API**, **Groq LLM (LLaMA 3)**, and **SpaCy**. Upload a resume and job description — get a smart JSON report that ranks the resume, extracts skills, calculates total experience, categorizes projects, and matches resume skills to the job requirement.

---

## 🚀 Features

- Upload a PDF Resume
- Select a Job Description
- Uses **Groq LLaMA 3** for deep resume analysis
- Extracts:
  - Skills mentioned in resume
  - Total years of experience
  - Project categories (e.g. AI, Web, Cloud)
  - Skill matching count
  - Relevance rank (0-100) to job description
- Returns response in **JSON format**
- Built using Django REST Framework and simple APIs

---

## 🧠 Sample JSON Output

```json
{
  "rank": "78%",
  "skills": ["Python", "Django", "REST API", "NLP"],
  "total_experience": "2 years",
  "project_category": ["Web Development", "AI"],
  "skills_matching": "4 out of 6 technical skills from Job Description"
}


## 🧰 Tech Stack

| Technology       | Used For                                 |
|------------------|------------------------------------------|
| Django           | Web framework and API routing            |
| Django REST      | Building RESTful APIs                    |
| SpaCy            | Light NLP tasks (can be expanded later)  |
| Groq API         | LLM-based analysis using LLaMA 3         |
| pdfplumber       | Extract text from PDF files              |
| SQLite (default) | Database                                 |
