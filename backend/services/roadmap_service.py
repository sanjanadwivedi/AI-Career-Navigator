import json

from ai.ai_service import generate
from ai.prompt_loader import get_prompt
from config import OPENAI_MODEL


def generate_roadmap(target_role, missing_skills):
    """
    Generate a personalized learning roadmap using AI.
    """

    messages = get_prompt(
        "roadmap-generator",
        target_role=target_role,
        missing_skills=json.dumps(
            missing_skills,
            indent=2
        ),
    )

    try:

        ai_response = generate(
            model=OPENAI_MODEL,
            messages=messages,
            temperature=0,
        )

        content = ai_response.content.strip()

        if content.startswith("```json"):
            content = content.replace("```json", "", 1)

        if content.endswith("```"):
            content = content[:-3]

        content = content.strip()

        roadmap = json.loads(content)

        return roadmap

    except Exception as e:

        print("Roadmap Generator Error:", e)

        return []