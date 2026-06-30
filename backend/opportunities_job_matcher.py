def calculate_job_match(user_skills, job_skills):

    matched_skills = []

    user_skills_lower = [
        skill.lower()
        for skill in user_skills
    ]

    for job_skill in job_skills:

        job_skill_lower = job_skill.lower()

        for user_skill in user_skills_lower:

            if (
                job_skill_lower in user_skill
                or
                user_skill in job_skill_lower
            ):
                matched_skills.append(job_skill)
                break

    score = round(
        (len(matched_skills) /
         max(len(job_skills), 1))
        * 100
    )

    return {
        "match_score": score,
        "matched_skills": matched_skills,
        "missing_skills": [
            skill
            for skill in job_skills
            if skill not in matched_skills
        ]
    }