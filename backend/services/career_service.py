from dotenv import load_dotenv
from safety import check_prompt_safety
from ai.ai_service import generate
from config import OPENAI_MODEL
from evaluations.evaluator import evaluate_response
from ai.prompt_loader import get_prompt

load_dotenv()


def career_chat(
    
    message,
    resume_analysis=None,
    selected_job=None,
):
    safety = check_prompt_safety(message)
    if not safety["safe"]:
        return {
        "response": safety["reason"],
        "evaluation": None,
    }
        
    context = ""

    if resume_analysis:
        context += f"""
Resume Analysis:
{resume_analysis}
"""

    if selected_job:
        context += f"""

Selected Job:

Title:
{selected_job.get("title")}

Company:
{selected_job.get("company")}

Description:
{selected_job.get("description")}
"""

    messages = get_prompt(
        "career-chat",
        context=context,
        message=message,
    )

    ai_response = generate(
        model=OPENAI_MODEL,
        messages=messages,
    )

    content = ai_response.content

    evaluation = evaluate_response(
        prompt_name="career-evaluator",
        inputs={
            "question": message,
        },
        response=content,
    )

    return {
        "response": content,
        "evaluation": evaluation,
    }