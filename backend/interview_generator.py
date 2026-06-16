import json
import re

from openai_client import client


def generate_interview_questions(
    resume_analysis,
    job_analysis
):

    prompt = f"""
Generate 10 interview questions based on:

Resume:
{resume_analysis}

Job Description:
{job_analysis}

Return ONLY valid JSON.

{{
    "interview_questions": []
}}
"""

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Return only valid JSON."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        text = response.choices[0].message.content

        text = re.sub(r"```json", "", text)
        text = re.sub(r"```", "", text)

        return json.loads(text.strip())

    except Exception as e:

        print(
            "Interview Generator Error:",
            e
        )

        return {
            "interview_questions": []
        }