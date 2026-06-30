import requests
from job_description_parser import parse_job_description

RAPIDAPI_KEY = 'b9d817481emsh8934fa8d804350ap13d461jsn3dc929658c71'


def get_jobs_by_role(role):

    url = "https://jsearch.p.rapidapi.com/search-v2"

    querystring = {
        "query": f"{role} jobs in India",
        "num_pages": "3",
        "country": "in",
        "date_posted": "all"
    }

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(
        url,
        headers=headers,
        params=querystring
    )

    
    data = response.json()
    jobs = []
    jobs_data = (
    data.get("data", {})
        .get("jobs", []))

    for item in jobs_data:
        description = item.get(
    "job_description",
    ""
)
        job_analysis = parse_job_description(
    description
)
        print(
    "JOB:",
    item.get("job_title")
)
        print(
    "EXTRACTED SKILLS:",
    job_analysis.get(
        "required_skills",
        []
    )
)
        jobs.append({
    "title": item.get("job_title"),
    "company": item.get("employer_name"),
    "location": item.get("job_city") or "Remote",
    "type": item.get("job_employment_type") or "Not Specified",
    "salary": "Not Disclosed",
    "apply_url": item.get("job_apply_link"),
    "description": description,
    "skills": job_analysis.get(
        "required_skills",
        []
    ),
    "company_logo": item.get("employer_logo"),
    "posted": item.get("job_posted_at_datetime_utc"),
})
    return jobs