def calculate_ats(resume):

    score = 0

    # Contact Info (15)
    if resume.get("email"):
        score += 8

    if resume.get("phone"):
        score += 7

    # Skills (25)
    skills_count = (
        len(resume.get("core_skills", []))
        + len(resume.get("frameworks_libraries", []))
        + len(resume.get("tools_platforms", []))
    )

    score += min(skills_count, 25)

    # Projects (20)
    projects = resume.get("projects", [])
    score += min(len(projects) * 5, 20)

    # Experience (20)
    experience = resume.get("experience", [])
    score += min(len(experience) * 10, 20)

    # Education (10)
    if resume.get("education"):
        score += 10

    # Links (10)
    if resume.get("github"):
        score += 5

    if resume.get("linkedin"):
        score += 5

    return min(score, 100)