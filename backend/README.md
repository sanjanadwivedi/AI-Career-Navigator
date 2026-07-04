# 🚀 AI Career Navigator

<p align="center">
  <img src="screenshots/home.png" alt="AI Career Navigator Banner" width="100%">
</p>

<p align="center">

![React](https://img.shields.io/badge/React-19-blue?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green?logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.11-yellow?logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4.1-black)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

## 🌐 Live Demo

### Frontend

https://beam-jobs-nine.vercel.app

### Backend API

https://ai-career-navigator-xwex.onrender.com

---

# 📖 Overview

AI Career Navigator is an AI-powered career assistant that helps job seekers optimize their resumes, evaluate ATS compatibility, analyze job descriptions, prepare for interviews, discover career opportunities, and receive personalized learning roadmaps.

Instead of using multiple career tools separately, AI Career Navigator combines resume analysis, job matching, AI coaching, dashboard analytics, and resume tailoring into one unified platform.

---

# ✨ Features

- 📄 AI Resume Analysis
- 🎯 ATS Score Prediction
- 💼 Resume vs Job Match Analysis
- 🤖 AI Career Coach
- 📝 AI Resume Tailoring
- 📊 Career Dashboard
- 📈 Resume Analytics
- 🎓 Personalized Learning Roadmap
- 💡 Interview Question Generation
- 📚 Skill Gap Analysis
- 📑 PDF Report Export
- ❤️ Save Jobs
- 🔍 AI Job Recommendations

---

# 🖼️ Screenshots

## Home

![Home](screenshots/home.png)

---

## Resume Analysis

![Resume](screenshots/resume-analysis.png)

---

## Job Match

![Job Match](screenshots/job-match.png)

---

## Career Dashboard

![Dashboard](screenshots/dashboard.png)

---

## AI Career Coach

![Career Coach](screenshots/ai-coach.png)

---

## Learning Roadmap

![Roadmap](screenshots/roadmap.png)

---

# 🏗️ Architecture

```
                Resume PDF
                     │
                     ▼
            AI Career Navigator
                     │
      ┌──────────────┼──────────────┐
      │              │              │
      ▼              ▼              ▼
 Resume Parser   ATS Analysis   Job Matching
      │              │              │
      └──────────────┼──────────────┘
                     ▼
             OpenAI GPT-4.1
                     │
                     ▼
        AI Insights & Recommendations
                     │
                     ▼
          Dashboard • Roadmap • PDF
```

---

# ⚙️ Tech Stack

## Frontend

- React 19
- TypeScript
- Vite
- TanStack Router
- Tailwind CSS
- Recharts
- React Hook Form
- Lucide Icons

---

## Backend

- FastAPI
- Python
- OpenAI GPT-4.1
- PyMuPDF
- ReportLab
- Pydantic

---

## Deployment

Frontend

- Vercel

Backend

- Render

---

# 📂 Project Structure

```
AI-Career-Navigator/
│
├── backend/
│   ├── ai/
│   ├── services/
│   ├── prompts/
│   ├── uploads/
│   ├── evaluations/
│   ├── main.py
│   └── requirements.txt
│
└── frontend/
    ├── src/
    ├── components/
    ├── routes/
    ├── context/
    └── package.json
```

---

# 🧠 AI Capabilities

The platform uses GPT-4.1 to generate:

- Resume evaluation
- ATS recommendations
- Resume summary
- Missing skills
- Career matching
- Personalized learning roadmap
- Resume improvements
- Interview questions
- Resume tailoring suggestions

---

# 🚀 Getting Started

## Clone the repositories

Backend

```bash
git clone https://github.com/sanjanadwivedi/AI-Career-Navigator.git
```

Frontend

```bash
git clone https://github.com/sanjanadwivedi/beam-jobs.git
```

---

## Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs at

```
http://localhost:8000
```

---

## Frontend

```bash
cd beam-jobs

npm install

npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

# 🔑 Environment Variables

Backend

Create a `.env`

```
OPENAI_API_KEY=your_key_here
```

Frontend

```
VITE_API_BASE_URL=http://localhost:8000
```

For production

```
VITE_API_BASE_URL=https://ai-career-navigator-xwex.onrender.com
```

---

# 📊 Workflow

```
Upload Resume
       │
       ▼
Extract Resume Text
       │
       ▼
AI Analysis
       │
       ├── ATS Score
       ├── Skills
       ├── Career Match
       ├── Improvements
       ├── Roadmap
       └── Interview Questions
       │
       ▼
Dashboard & Reports
```

---

# 📌 Future Improvements

- Authentication
- User Accounts
- Resume History
- Job Tracking
- Company Insights
- AI Mock Interviews
- LinkedIn Profile Analysis
- Cover Letter Generator
- Salary Prediction
- Recruiter Dashboard

---

# 🤝 Contributing

Contributions are welcome.

If you'd like to improve AI Career Navigator, feel free to fork the repository and submit a pull request.

---

# 👩‍💻 Author

**Sanjana Dwivedi**

GitHub

https://github.com/sanjanadwivedi

LinkedIn

(Add your LinkedIn profile)

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

It helps others discover the project and motivates future development.

---

<p align="center">

Built with ❤️ using React, FastAPI and OpenAI GPT-4.1

</p>
