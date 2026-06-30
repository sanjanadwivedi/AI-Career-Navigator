import json

from ai.prompt_loader import get_prompt
from ai.ai_service import generate
from config import OPENAI_MODEL


def tailor_resume(resume_analysis, job_analysis):

    prompt = get_prompt(
        "resume-tailor",
        resume_analysis=json.dumps(resume_analysis, indent=2),
        job_analysis=json.dumps(job_analysis, indent=2),
    )

    try:
        response = generate(
            model=OPENAI_MODEL,
            temperature=0.4,
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
        print("Resume Tailor Error:", e)

        return {
            "tailored_summary": "",
            "optimized_bullets": [],
            "keywords_added": [],
            "skills_to_highlight": [],
            "missing_keywords": [],
            "ats_improvements": [],
        }