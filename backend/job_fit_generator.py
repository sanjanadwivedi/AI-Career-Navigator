import json
import re

from openai_client import client


def generate_job_fit_content(
    resume_analysis,
    job_analysis,
    match_result
):

    prompt = f"""
You are an expert recruiter and career coach.

Candidate Resume:
{resume_analysis}

Job Description Analysis:
{job_analysis}

Match Result:
{match_result}

Return ONLY valid JSON.

{{
  "resume_improvements": [],
  "interview_questions": [],
  "roadmap": [
    {{
      "phase": "",
      "focus": ""
    }}
  ]
}}

Requirements:

1. Give 5 specific resume improvements.
2. Generate 8 interview questions tailored to the role.
3. Generate a 4-step career roadmap.
4. Return valid JSON only.
"""

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert recruiter. "
                        "Return ONLY valid JSON."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        text = response.choices[0].message.content

        print("\n===== JOB FIT RESPONSE =====")
        print(text)
        print("============================\n")

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

        return json.loads(
            text.strip()
        )

    except Exception as e:

        print(
            "Job Fit Generator Error:",
            e
        )

        return {
            "resume_improvements": [],
            "interview_questions": [],
            "roadmap": []
        }