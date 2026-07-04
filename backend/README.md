# 🚀 AI Career Navigator – Backend

> FastAPI backend powering the AI Career Navigator platform with AI-powered resume analysis, ATS scoring, job matching, career coaching, roadmap generation, and PDF report generation.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.136-green?logo=fastapi)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT-black?logo=openai)
![Render](https://img.shields.io/badge/Deployment-Render-46E3B7)
![License](https://img.shields.io/badge/License-MIT-blue)

---

# 🌐 Live Application

### 🚀 Frontend

https://beam-jobs-nine.vercel.app

### ⚡ Backend API

https://ai-career-navigator-xwex.onrender.com

---

# 📌 Overview

AI Career Navigator is an AI-powered career guidance platform designed to help students and professionals improve their resumes, identify skill gaps, match jobs, receive AI career guidance, and generate personalized career roadmaps.

This repository contains the **FastAPI backend** that powers all AI functionalities.

---

# ✨ Backend Features

- 📄 Resume Parsing
- 🎯 ATS Score Calculation
- 💼 Resume & Job Matching
- 🤖 AI Career Coach
- 🛣 AI Roadmap Generator
- ✍ Resume Tailoring
- 📑 PDF Report Generation
- 📊 Langfuse AI Monitoring
- ⚡ REST API

---

# 🛠 Tech Stack

- Python 3.11
- FastAPI
- OpenAI GPT
- Langfuse
- PyMuPDF
- ReportLab
- Uvicorn
- Render

---

# 🏗 System Architecture

```text
                    AI Career Navigator

           React + TypeScript Frontend
                     │
                     ▼
               FastAPI Backend
                     │
      ┌──────────────┼───────────────┐
      │              │               │
 Resume Parser   ATS Engine   Career Coach
      │              │               │
      ├──────────────┼───────────────┤
      │              │               │
 Job Matcher   Roadmap Generator PDF Generator
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
├── career_matcher.py
├── job_search.py
├── ats_scorer.py
├── pdf_generator.py
├── requirements.txt
├── Procfile
└── runtime.txt
```

---

# 🔗 API Endpoints

| Endpoint           | Description            |
| ------------------ | ---------------------- |
| `/`                | Health Check           |
| `/resume-analysis` | Analyze Resume         |
| `/job-match`       | Resume vs Job Matching |
| `/career-coach`    | AI Career Guidance     |
| `/roadmap`         | Personalized Roadmap   |
| `/tailor-resume`   | Resume Tailoring       |

---

# 🚀 Run Locally

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

The complete user interface is available here:

**Frontend Repository**

https://github.com/sanjanadwivedi/beam-jobs

**Live Demo**

https://beam-jobs-nine.vercel.app

---

# 👩‍💻 Developed By

**Sanjana Dwivedi**

Computer Science Undergraduate | AI & Data Analytics Enthusiast

---

⭐ If you found this project useful, consider giving the repository a star!
