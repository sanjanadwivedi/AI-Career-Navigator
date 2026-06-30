def match_resume_to_job(
    resume_skills,
    job_skills
):

    matched_skills = []
    missing_skills = []

    resume_skills_lower = [
        skill.lower().strip()
        for skill in resume_skills
    ]

    skill_aliases = {
        "microsoft excel": ["excel"],
        "excel": ["microsoft excel"],

        "dashboard creation": [
            "power bi",
            "tableau",
            "data visualization",
            "data visualisation"
        ],
        "LLMs": [
    "transformers",
    "llm",
    "chatbot"
],

        "data analysis": [
            "statistical analysis",
            "analytical thinking",
            "data visualization",
            "data visualisation"
        ],

        "machine learning": [
            "ml modelling",
            "ml modeling"
        ],

        "statistical analysis": [
            "statistics",
            "data analysis"
        ],

        "communication skills": [
            "communication",
            "team collaboration"
        ],

        "presentation skills": [
            "communication",
            "report writing"
        ],
        "Data Preprocessing": [
    "data cleaning",
    "data preprocessing",
    "normalisation",
    "pipeline"
],
        "Attention to Detail": [
    "quality",
    "evaluation",
    "accuracy",
    "validation"
]
    }

    for job_skill in job_skills:

        job_skill_lower = job_skill.lower().strip()

        found = False

        # Direct / partial matching
        for resume_skill in resume_skills_lower:

            if (
                job_skill_lower in resume_skill
                or resume_skill in job_skill_lower
            ):
                found = True
                break

        # Alias matching
        if not found:

            aliases = skill_aliases.get(
                job_skill_lower,
                []
            )

            for alias in aliases:

                if any(
                    alias in skill
                    for skill in resume_skills_lower
                ):
                    found = True
                    break

        if found:
            matched_skills.append(job_skill)
        else:
            missing_skills.append(job_skill)

    score = round(
        (
            len(matched_skills)
            / len(job_skills)
        ) * 100
    ) if job_skills else 0

    return {
        "match_score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }
    
