import json
import re

from openai_client import client


def generate_resume_improvements(
    resume_analysis,
    job_analysis,
    match_result
):

    prompt = f"""
You are an expert Resume Reviewer and Recruiter.

Analyze:

1. Candidate Resume
2. Job Description
3. Match Results

Return ONLY valid JSON.

Format:

{{
    "resume_improvements": [],
    "high_priority_changes": [],
    "keywords_to_add": []
}}

Focus on:

- Missing skills
- ATS improvements
- Stronger resume bullets
- Keywords from job description
- Recruiter expectations

Resume Analysis:

{resume_analysis}

Job Analysis:

{job_analysis}

Match Result:

{match_result}
"""

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert ATS Resume Reviewer. "
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

        print("\n===== OPENAI RESUME IMPROVEMENTS =====")
        print(text)
        print("=====================================\n")

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

        text = text.strip()

        return json.loads(text)

    except Exception as e:

        print(
            "Resume Improver Error:",
            e
        )

        return {
            "resume_improvements": [],
            "high_priority_changes": [],
            "keywords_to_add": []
        }