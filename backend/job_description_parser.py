import json
import re
import hashlib

from ai.openai_client import client

jd_cache = {}

def parse_job_description(job_description):

    cache_key = hashlib.md5(
        job_description.encode()
    ).hexdigest()

    if cache_key in jd_cache:
        return jd_cache[cache_key]

    prompt = f"""
Analyze the following job description.

Return ONLY valid JSON.

Job Description:
{job_description}

Return exactly:

{{
    "job_title": "",
    "required_skills": [],
    "preferred_skills": [],
    "responsibilities": [],
    "education_requirements": [],
    "keywords": []
}}
"""

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert job description analyzer. Always return valid JSON only."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        text = response.choices[0].message.content


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

        result = json.loads(
            text.strip()
        )

        jd_cache[cache_key] = result

        return result

    except Exception as e:

        print(
            "JD Parser Error:",
            e
        )

        return {
            "job_title": "Unknown",
            "required_skills": [],
            "preferred_skills": [],
            "responsibilities": [],
            "education_requirements": [],
            "keywords": []
        }