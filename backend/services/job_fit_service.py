import json

from ai.prompt_loader import get_prompt
from ai.ai_service import generate
from config import OPENAI_MODEL


def generate_job_fit_content(
    resume_analysis,
    job_analysis,
    match_result,
):
    prompt = get_prompt(
        "job-fit-generator",
        resume_analysis=json.dumps(resume_analysis, indent=2),
        job_analysis=json.dumps(job_analysis, indent=2),
        match_result=json.dumps(match_result, indent=2),
    )

    try:
        response = generate(
            model=OPENAI_MODEL,
            temperature=0.3,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            response_format={
                "type": "json_object"
            },
        )

        return json.loads(response.content)

    except Exception as e:
        print("Job Fit Generator Error:", e)

        return {
            "resume_improvements": [],
            "interview_questions": [],
            "roadmap": [],
        }