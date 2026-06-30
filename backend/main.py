from fastapi import FastAPI, UploadFile, File
import shutil
import os
import json
import re
from ai.openai_client import client
from services.career_match_service import generate_career_match
from job_search import get_jobs_by_role
from services.job_fit_service import (
    generate_job_fit_content
)
from resume_parser import extract_text
from services.resume_service import parse_resume_with_openai
from services. roadmap_service import generate_roadmap
from ats_scorer import calculate_ats_score
from fastapi.responses import FileResponse

from info_extractor import (
    extract_name,
    extract_email,
    extract_phone
)

from pydantic import BaseModel
from job_description_parser import parse_job_description
from resume_job_matcher import match_resume_to_job
from fastapi import Form
from fastapi.middleware.cors import CORSMiddleware
from services.resume_tailor import tailor_resume
from pdf_generator import create_report
from services.career_service import career_chat
from opportunities_job_matcher import calculate_job_match

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://127.0.0.1:8080",
        "http://192.168.1.10:8080",
        "http://192.168.1.6:8080",
        "http://192.168.1.9:8080",
    "http://192.168.1.11:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RoadmapRequest(BaseModel):
    skills: list[str]
    
class JobRequest(BaseModel):
    job_description: str

class JobRecommendationRequest(BaseModel):
    role: str
    skills: list[str]

class ResumeJobRequest(BaseModel):
    resume_analysis: dict
    job_description: str
    
class CareerChatRequest(BaseModel):
    message: str
    resume_analysis: dict | None = None
    selected_job: dict | None = None

@app.get("/")
def home():
    return {
        "message": "AI Career Navigator API Running"
    }


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    # Create uploads folder if not exists
    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text from resume
    text = extract_text(file_path)

    # Gemini Analysis
    resume_analysis = parse_resume_with_openai(text)
    ats_result = calculate_ats_score(
    resume_analysis
)
    rule_based_ats = ats_result["score"]
    resume_analysis["ats_breakdown"] = (
    ats_result["breakdown"]
)
    gemini_ats = resume_analysis.get("ats_score")
    if isinstance(gemini_ats, (int, float)):
        final_ats = round(
        (0.7 * rule_based_ats) +
        (0.3 * gemini_ats)
    )
    else:
        final_ats = rule_based_ats
    resume_analysis["ats_score"] = final_ats
    print(resume_analysis)

    # Override Gemini values with regex extraction
    resume_analysis["name"] = extract_name(text)
    resume_analysis["email"] = extract_email(text)
    resume_analysis["phone"] = extract_phone(text)

    # Safe role selection
    career_match = generate_career_match(
        resume_analysis
)
    role_matches = career_match.get("role_matches", [])
    recommended_roles = career_match.get("recommended_roles", [])

    resume_analysis["recommended_roles"] = recommended_roles

    if role_matches:
        missing_skills = role_matches[0].get("missing_skills", [])
    else:
        missing_skills = []

    resume_analysis["missing_skills"] = missing_skills
    resume_analysis["weaknesses"] = missing_skills[:5]

    if recommended_roles:
        target_role = recommended_roles[0]
    else:
        target_role = "Data Analyst"

    roadmap = generate_roadmap(
        target_role,
        missing_skills
    )

    return {
        "resume_analysis": resume_analysis,
        "career_match": career_match,
        "role_matches": role_matches,
        "roadmap": roadmap,
    }
    
@app.post("/job-analysis")
async def job_analysis(request: JobRequest):

    job_analysis = parse_job_description(
        request.job_description
    )

    return {
        "job_analysis": job_analysis
    }
@app.post("/analyze-job-fit")
async def analyze_job_fit(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    # Save uploaded resume
    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract resume text
    text = extract_text(file_path)

    # Resume Analysis
    resume_analysis = parse_resume_with_openai(text)

    # Override contact details using regex
    resume_analysis["name"] = extract_name(text)
    resume_analysis["email"] = extract_email(text)
    resume_analysis["phone"] = extract_phone(text)

    # Job Description Analysis
    job_analysis = parse_job_description(
        job_description
    )

    # Collect Resume Skills
    all_skills = (
        resume_analysis.get("core_skills", [])
        + resume_analysis.get("frameworks_libraries", [])
        + resume_analysis.get("tools_platforms", [])
    )
    
    # Match Resume vs JD
    job_match = match_resume_to_job(
        all_skills,
        job_analysis.get("required_skills", [])
    )

    # Generate Resume Improvements
    job_fit_content = generate_job_fit_content(
    resume_analysis,
    job_analysis,
    job_match
)
    return {

    "resume_analysis": resume_analysis,

    "job_analysis": job_analysis,

    "job_match": job_match,

    "resume_improvements":
        job_fit_content[
            "resume_improvements"
        ],

    "interview_questions":
        job_fit_content[
            "interview_questions"
        ],

    "roadmap":
        job_fit_content[
            "roadmap"
        ]
}
@app.post("/tailor-resume")
async def tailor_resume_endpoint(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(file_path)

    resume_analysis = parse_resume_with_openai(text)

    job_analysis = parse_job_description(job_description)

    result = tailor_resume(
        resume_analysis,
        job_analysis
    )

    return result


@app.post("/career-chat")
async def career_chat_api(request: CareerChatRequest):

    return career_chat(
        request.message,
        request.resume_analysis,
        request.selected_job,
    )



@app.post("/export-report")
async def export_report(data: dict):

    pdf_file = create_report(data)

    return FileResponse(
        path=pdf_file,
        media_type="application/pdf",
        filename="CareerNavigator_Report.pdf"
    )

@app.get("/jobs/{role}")
async def get_jobs(role: str):

    jobs = get_jobs_by_role(role)

    # Temporary user skills
    user_skills = [
        "SQL",
        "Excel",
        "Power BI",
        "Python"
    ]

    for job in jobs:

        match = calculate_job_match(
            user_skills,
            job["skills"]
        )

        job["match_score"] = match["match_score"]

        job["matched_skills"] = match["matched_skills"]

        job["missing_skills"] = match["missing_skills"]
        score = match["match_score"]
        if score >= 80:
            insight = (
        "Strong match. Your profile aligns well with this role."
    )
        elif score >= 60:
            insight = (
        "Good match. Learning missing skills can improve your fit."
    )
        else:
            insight = (
        "Moderate match. Focus on the missing skills before applying."
    )
        job["ai_insight"] = insight

    return {
        "role": role,
        "jobs": jobs
    }


@app.post("/job-recommendations")

async def job_recommendations(
    request: JobRecommendationRequest
):

    jobs = get_jobs_by_role(
        request.role
    )
    for job in jobs:

        match = calculate_job_match(
            request.skills,
            job["skills"]
        )

        job["match_score"] = (
            match["match_score"]
        )

        job["matched_skills"] = (
            match["matched_skills"]
        )

        job["missing_skills"] = (
            match["missing_skills"]
        )
        score = match["match_score"]
        if score >= 80:
            job["ai_insight"] = (
        "Strong match. Your profile aligns well with this role."
    )
        elif score >= 60:
            job["ai_insight"] = (
        "Good match. Learning the missing skills can improve your fit."
    )
        else:
            job["ai_insight"] = (
        "Moderate match. Focus on building the missing skills before applying."
    )

    return {
        "role": request.role,
        "jobs": jobs
    }
class RoadmapRequest(BaseModel):
    skills: list[str]


@app.post("/generate-roadmap")
async def generate_roadmap_api(
    request: RoadmapRequest
):

    prompt = f"""
Create a learning roadmap for these skills:

{request.skills}

Return ONLY valid JSON.

[
  {{
    "phase": "",
    "skill": "",
    "resources": [],
    "project": "",
    "timeline": ""
  }}
]
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    text = response.choices[0].message.content

    text = re.sub(
        r"```json",
        "",
        text
    )

    text = re.sub(
        r"```",
        "",
        text
    )

    return json.loads(
        text.strip()
    )
class ResumeTailorRequest(BaseModel):
    resume_analysis: dict
    job_description: str

@app.post("/tailor-resume-ai")
async def tailor_resume_ai(
    request: ResumeTailorRequest
):

    job_analysis = parse_job_description(
        request.job_description
    )

    result = tailor_resume(
        request.resume_analysis,
        job_analysis
    )

    return result