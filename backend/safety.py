import json

from ai.ai_service import generate
from config import OPENAI_MODEL
from ai.prompt_loader import get_prompt


def check_prompt_safety(message: str):

    prompt = get_prompt(
        "safety-classifier",
        message=message,
    )

    ai_response = generate(
        model=OPENAI_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0,
    )

    return json.loads(ai_response.content)