import google.generativeai as genai
import json
import os
import re

from dotenv import load_dotenv

load_dotenv()
print("API KEY:", os.getenv("GEMINI_API_KEY"))

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


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

experience_level:
Choose exactly one from:

Student
Fresher
Junior
Mid-Level
Senior

Determine based on education, internships, and work experience.

Rules:

1. Separate skills into categories.
2. Generate a 2-3 line professional profile summary.
3. List top strengths.
4. List top weaknesses.
5. Identify missing skills.
6. Estimate ATS score realistically.
7. Return ONLY valid JSON.
8. recommended_roles should contain suitable career paths with confidence scores.


recommended_roles format:

[
  {{
    "role": "Data Analyst",
    "confidence": 95
  }}
]

ats_score:
integer between 0 and 100

missing_skills:
list of important missing skills for the best matching role

ats_improvements:
list of suggestions to improve ATS performance

Think like:
- ATS software
- Technical recruiter
- Hiring manager

Do not inflate scores.

If GitHub or LinkedIn links are not found,
return null instead of an empty string.

For name extraction:

- Extract the candidate's full name only.
- Do NOT include words like:
  I
  I'm
  I am
  My
  Myself

Return only the actual candidate name.

Return JSON in this format:

{{
  "name": "",
  "email": "",
  "phone": "",

  "profile_summary": "",

  "recommended_roles": [
    {{
      "role": "",
      "confidence": 0
    }}
  ],

  "core_skills": [],
  "frameworks_libraries": [],
  "tools_platforms": [],
  "soft_skills": [],

  "education": [],
  "projects": [],
  "experience": [],

  "strengths": [],
  "weaknesses": [],

  "missing_skills": [],
   "experience_level": "",
  "ats_score": 0,

  "ats_improvements": []
  
  "github": "",
  "linkedin": ""
}}

Resume:

{resume_text}
"""

    try:

        response = model.generate_content(prompt)

        text = response.text

        text = re.sub(r"```json", "", text)
        text = re.sub(r"```", "", text)

        text = text.strip()

        parsed_json = json.loads(text)
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
            "experience_level"
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

        return {
            "error": str(e),
            "raw_response": text if "text" in locals() else None
        }