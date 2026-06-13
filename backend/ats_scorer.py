def calculate_ats_score(resume_analysis):

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
    if len(resume_analysis.get("core_skills", [])) > 0:
        skills_score = 25

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
    if len(resume_analysis.get("experience", [])) > 0:
        experience_score = 25

    # Education (10)
    if len(resume_analysis.get("education", [])) > 0:
        education_score = 10

    total_score = (
        contact_score +
        skills_score +
        projects_score +
        experience_score +
        education_score
    )

    # Deductions
    if not resume_analysis.get("github"):
        total_score -= 3

    if not resume_analysis.get("linkedin"):
        total_score -= 3

    total_score = max(0, total_score)

    return {
        "score": min(total_score, 100),

        "breakdown": {
            "contact_info": contact_score,
            "skills": skills_score,
            "projects": projects_score,
            "experience": experience_score,
            "education": education_score
        }
    }