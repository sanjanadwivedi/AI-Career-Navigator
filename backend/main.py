from fastapi import FastAPI, UploadFile, File
import shutil
import os

from job_fit_generator import (
    generate_job_fit_content
)
from resume_parser import extract_text
from gemini_parser import parse_resume_with_gemini
from career_matcher import calculate_match, ROLE_DATABASE
from roadmap_generator import generate_roadmap
from ats_scorer import calculate_ats_score
from career_matcher import (
    calculate_match,
    calculate_all_role_matches,
    ROLE_DATABASE
)

from info_extractor import (
    extract_name,
    extract_email,
    extract_phone
)

from pydantic import BaseModel
from job_description_parser import parse_job_description
from job_matcher import match_resume_to_job
from resume_improver import generate_resume_improvements
from fastapi import Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://192.168.1.7:8080",
        "http://192.168.1.11:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class JobRequest(BaseModel):
    job_description: str


class ResumeJobRequest(BaseModel):
    resume_analysis: dict
    job_description: str

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
    resume_analysis = parse_resume_with_gemini(text)
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

    print("\n===== GEMINI RESPONSE =====")
    print(resume_analysis)
    print("===========================\n")

    # Override Gemini values with regex extraction
    resume_analysis["name"] = extract_name(text)
    resume_analysis["email"] = extract_email(text)
    resume_analysis["phone"] = extract_phone(text)

    # Safe role selection
    if (
        "recommended_roles" in resume_analysis
        and isinstance(resume_analysis["recommended_roles"], list)
        and len(resume_analysis["recommended_roles"]) > 0
    ):

        recommended_role = resume_analysis["recommended_roles"][0]["role"]

        if recommended_role in ROLE_DATABASE:
            target_role = recommended_role
        else:
            target_role = "Data Analyst"

    else:
        target_role = "Data Analyst"

    # Collect all skills
    all_skills = (
        resume_analysis.get("core_skills", [])
        + resume_analysis.get("frameworks_libraries", [])
        + resume_analysis.get("tools_platforms", [])
    )

    # Career Match
    career_match = calculate_match(
        all_skills,
        target_role
    )
    role_matches = calculate_all_role_matches(
    all_skills)
    
    # Roadmap
    roadmap = generate_roadmap(
        career_match["missing_skills"]
    )

    return {
        "resume_analysis": resume_analysis,
        "career_match": career_match,
        "role_matches": role_matches,
        "roadmap": roadmap
        
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
    resume_analysis = parse_resume_with_gemini(text)

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