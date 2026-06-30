import json

from ats_calculator import calculate_ats
from ai.prompt_loader import get_prompt
from ai.ai_service import generate


def parse_resume_with_openai(resume_text):
    prompt = get_prompt(
        "resume-analyzer",
        resume=resume_text,
    )

    try:
        ai_response = generate(
            model="gpt-4o-mini",
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            response_format={
                "type": "json_object",
            },
        )

        parsed_json = json.loads(ai_response.content)

        parsed_json["weaknesses"] = []
        parsed_json["missing_skills"] = []
        parsed_json["ats_score"] = calculate_ats(parsed_json)

        parsed_json["github"] = parsed_json.get("github") or ""
        parsed_json["linkedin"] = parsed_json.get("linkedin") or ""

        required_keys = [
            "name",
            "email",
            "phone",
            "profile_summary",
            "recommended_roles",
            "core_skills",
            "frameworks_libraries",
            "tools_platforms",
            "soft_skills",
            "education",
            "projects",
            "experience",
            "strengths",
            "weaknesses",
            "missing_skills",
            "ats_score",
            "ats_improvements",
            "experience_level",
            "github",
            "linkedin",
        ]

        for key in required_keys:
            if key not in parsed_json:

                if key == "ats_score":
                    parsed_json[key] = 0

                elif key in [
                    "name",
                    "email",
                    "phone",
                    "profile_summary",
                    "experience_level",
                    "github",
                    "linkedin",
                ]:
                    parsed_json[key] = ""

                else:
                    parsed_json[key] = []

        return parsed_json

    except Exception as e:
        print("Resume Parser Error:", e)

        return {
            "error": str(e),
        }