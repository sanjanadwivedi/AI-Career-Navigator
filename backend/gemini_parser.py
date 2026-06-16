from openai_client import client
import json
import re

def parse_resume_with_gemini(resume_text):

    prompt = f"""
You are an expert AI Resume Analyzer.

Analyze the resume and return ONLY valid JSON.

Use EXACT keys:

name
email
phone
profile_summary
recommended_roles
core_skills
frameworks_libraries
tools_platforms
soft_skills
education
projects
experience
strengths
weaknesses
missing_skills
ats_score
ats_improvements
experience_level
github
linkedin

Return valid JSON only.

Resume:

{resume_text}
"""

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert ATS Resume Analyzer. "
                        "Return ONLY valid JSON."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        text = response.choices[0].message.content

        print("\n===== OPENAI RESUME RESPONSE =====")
        print(text)
        print("=================================\n")

        text = re.sub(
            r"```json",
            "",
            text
        )

        text = re.sub(
            r"```",
            "",
            text
        )

        parsed_json = json.loads(
            text.strip()
        )

        if parsed_json.get("github") is None:
            parsed_json["github"] = ""

        if parsed_json.get("linkedin") is None:
            parsed_json["linkedin"] = ""

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
            "linkedin"
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
                    "linkedin"
                ]:
                    parsed_json[key] = ""

                else:
                    parsed_json[key] = []

        return parsed_json

    except Exception as e:

        print(
            "Resume Parser Error:",
            e
        )

        return {
            "error": str(e),
            "raw_response": text if "text" in locals() else None
        }