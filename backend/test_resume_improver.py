from resume_improver import (
    generate_resume_improvements
)

resume_analysis = {
    "core_skills": [
        "Python",
        "SQL",
        "Power BI"
    ]
}

job_analysis = {
    "job_title": "Data Analyst",

    "required_skills": [
        "Python",
        "SQL",
        "Power BI",
        "Statistics"
    ]
}

match_result = {
    "match_score": 75,
    "missing_skills": [
        "Statistics"
    ]
}

result = generate_resume_improvements(
    resume_analysis,
    job_analysis,
    match_result
)

print(result)