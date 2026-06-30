import json

from ai.ai_service import generate
from ai.prompt_loader import get_prompt
from config import OPENAI_MODEL


def generate_career_match(resume_analysis: dict):
    """
    Uses AI to determine the best career matches
    based on the analyzed resume.
    """

    messages = get_prompt(
        "career-matcher",
        resume_analysis=json.dumps(
            resume_analysis,
            indent=2
        ),
    )

    ai_response = generate(
        model=OPENAI_MODEL,
        messages=messages,
        temperature=0,
        response_format={
            "type": "json_object"
        },
    )

    return json.loads(
        ai_response.content
    )
if __name__ == "__main__":

    sample = {
        "core_skills": [
            "Python",
            "SQL",
            "Machine Learning"
        ],
        "projects": [
            {
                "name": "AI Career Navigator"
            }
        ]
    }

    result = generate_career_match(sample)

    print(result)