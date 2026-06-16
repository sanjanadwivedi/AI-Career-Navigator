from interview_generator import (
    generate_interview_questions
)

resume_analysis = {
    "core_skills": [
        "Python",
        "SQL",
        "Power BI"
    ],

    "projects": [
        {
            "title": "NLP Text Analytics Pipeline"
        }
    ]
}

job_analysis = {
    "job_title": "Data Analyst",

    "required_skills": [
        "Python",
        "SQL",
        "Statistics",
        "Power BI"
    ]
}

result = generate_interview_questions(
    resume_analysis,
    job_analysis
)

print(result)