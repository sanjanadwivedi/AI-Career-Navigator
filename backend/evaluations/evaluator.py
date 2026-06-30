import json

from ai.ai_service import generate
from config import EVALUATION_MODEL
from ai.prompt_loader import get_prompt


def evaluate_response(
    *,
    prompt_name: str,
    inputs: dict,
    response: str,
):
    """
    Generic LLM-as-a-Judge evaluator.
    """

    messages = get_prompt(
        prompt_name,
        **inputs,
        response=response,
    )

    ai_response = generate(
    model=EVALUATION_MODEL,
    messages=messages,
    temperature=0,
    response_format={
        "type": "json_object"
    },
)
    return json.loads(ai_response.content)