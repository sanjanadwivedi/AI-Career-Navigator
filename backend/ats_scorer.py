def calculate_ats_score(resume_analysis):
    bonus_score = 0
    contact_score = 0
    skills_score = 0
    projects_score = 0
    experience_score = 0
    education_score = 0

    # Contact Info (15)
    if resume_analysis.get("name"):
        contact_score += 5

    if resume_analysis.get("email"):
        contact_score += 5

    if resume_analysis.get("phone"):
        contact_score += 5

    # Skills (25)
    total_skills = (
    len(resume_analysis.get("core_skills", []))
    + len(resume_analysis.get("frameworks_libraries", []))
    + len(resume_analysis.get("tools_platforms", []))
)
    if total_skills >= 12:
        skills_score = 25
    
    elif total_skills >= 8:
        skills_score = 20
    
    elif total_skills >= 5:
        skills_score = 15
    
    elif total_skills >= 3:
        skills_score = 10

    # Projects (25)
    project_count = len(
        resume_analysis.get("projects", [])
    )

    if project_count >= 3:
        projects_score = 25

    elif project_count == 2:
        projects_score = 20

    elif project_count == 1:
        projects_score = 10

    # Experience (25)
    experience_count = len(
    resume_analysis.get("experience", [])
)
    if experience_count >= 2:
        experience_score = 25
    
    elif experience_count == 1:
        experience_score = 20

    # Education (10)
    if len(resume_analysis.get("education", [])) > 0:
        education_score = 10
    # GitHub & LinkedIn Bonus
    if resume_analysis.get("github"):
        bonus_score += 3
    if resume_analysis.get("linkedin"):
        bonus_score += 3
    
    total_score = (
    contact_score +
    skills_score +
    projects_score +
    experience_score +
    education_score +
    bonus_score
)
   
    # Deductions
    total_score = max(0, total_score)

    return {
        "score": min(total_score, 100),

        "breakdown": {
    "contact_info": contact_score,
    "skills": skills_score,
    "projects": projects_score,
    "experience": experience_score,
    "education": education_score,
    "bonus": bonus_score
}
    }