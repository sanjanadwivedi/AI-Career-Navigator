# 🚀 AI Career Navigator – Backend

<p align="center">
  <strong>FastAPI backend powering an AI-driven career development platform.</strong><br>
  Resume Analysis • ATS Scoring • Job Matching • AI Career Coach • Roadmaps
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-009688?logo=fastapi&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT-412991?logo=openai&logoColor=white)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?logo=render)
![License](https://img.shields.io/badge/License-MIT-blue)

</p>

---

# 🌐 Live Application

### 🎯 Frontend

https://beam-jobs-nine.vercel.app

### ⚡ Backend API

https://ai-career-navigator-xwex.onrender.com

---

# 📌 About

AI Career Navigator is an AI-powered career development platform designed to help students and professionals improve their resumes, identify skill gaps, match jobs with their profiles, receive personalized AI career guidance, and generate structured learning roadmaps.

This repository contains the **FastAPI backend** responsible for all AI processing and business logic.

---

# ✨ Backend Features

- 📄 Resume Parsing
- 🎯 ATS Score Calculation
- 💼 Resume vs Job Matching
- 🤖 AI Career Coach
- 🛣 Personalized Career Roadmaps
- ✍ AI Resume Tailoring
- 📑 PDF Report Generation
- 📊 Langfuse AI Monitoring
- ⚡ REST API

---

# 🛠 Tech Stack

| Category          | Technologies |
| ----------------- | ------------ |
| Language          | Python 3.11  |
| Framework         | FastAPI      |
| AI                | OpenAI GPT   |
| Monitoring        | Langfuse     |
| PDF Processing    | PyMuPDF      |
| Report Generation | ReportLab    |
| Server            | Uvicorn      |
| Deployment        | Render       |

---

# 🏗 Architecture

```text
                     AI Career Navigator

              React + TypeScript Frontend
                        │
                        ▼
                 FastAPI REST Backend
                        │
      ┌─────────────────┼─────────────────┐
      │                 │                 │
 Resume Parser      ATS Engine      Career Coach
      │                 │                 │
      ├─────────────────┼─────────────────┤
      │                 │                 │
 Job Matcher     Resume Tailor     Roadmap Generator
                        │
                        ▼
                   OpenAI GPT API
                        │
                        ▼
                    Langfuse Logs
```

---

# 📂 Project Structure

```text
backend/
│
├── ai/
├── evaluations/
├── models/
├── prompts/
├── services/
├── uploads/
│
├── main.py
├── ats_scorer.py
├── career_matcher.py
├── job_search.py
├── pdf_generator.py
├── requirements.txt
├── Procfile
└── runtime.txt
```

---

# 🔗 API Endpoints

| Endpoint           | Description                        |
| ------------------ | ---------------------------------- |
| `/`                | Health Check                       |
| `/resume-analysis` | Analyze uploaded resume            |
| `/job-match`       | Resume vs Job Description matching |
| `/career-coach`    | AI-powered career guidance         |
| `/roadmap`         | Personalized career roadmap        |
| `/tailor-resume`   | Resume optimization                |

---

# 🚀 Running Locally

```bash
git clone https://github.com/sanjanadwivedi/AI-Career-Navigator.git

cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

---

# 🌐 Frontend

The complete frontend implementation, UI screenshots and source code are available here.

### Live Demo

https://beam-jobs-nine.vercel.app

### Frontend Repository

https://github.com/sanjanadwivedi/beam-jobs

---

# 🚀 Future Improvements

- User Authentication
- Resume History
- AI Mock Interviews
- Skill Gap Analytics
- Company-specific Resume Optimization
- Job Recommendation Engine
- Multi-language Support

---

# 👩‍💻 Developed By

**Sanjana Dwivedi**

Computer Science Undergraduate • AI & Data Analytics Enthusiast

---

⭐ If you found this project useful, consider giving it a star.
