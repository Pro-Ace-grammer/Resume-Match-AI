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
```


## 🧰 Tech Stack

| Technology       | Used For                                 |
|------------------|------------------------------------------|
| Django           | Web framework and API routing            |
| Django REST      | Building RESTful APIs                    |
| SpaCy            | Light NLP tasks (can be expanded later)  |
| Groq API         | LLM-based analysis using LLaMA 3         |
| pdfplumber       | Extract text from PDF files              |
| SQLite (default) | Database                                 |



## 🛠️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/resume-match-ai.git
cd resume-match-ai
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Migrate Database
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Run Server
```bash
python manage.py runserver
```

## ⚠️ Known Limitations
```text
❌ Basic error handling; no UI (API only)
📄 Resume parser is simple — no deep NLP yet
🤖 Groq call assumes valid PDF and JD inputs
🔐 No authentication system
