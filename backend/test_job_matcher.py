from job_matcher import match_resume_to_job

resume_skills = [
    "Python",
    "SQL",
    "Power BI",
    "Tableau"
]

job_skills = [
    "Python",
    "SQL",
    "Power BI",
    "Statistics"
]

result = match_resume_to_job(
    resume_skills,
    job_skills
)

print(result)