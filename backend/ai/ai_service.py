import logging

from openai import APIError, APITimeoutError, RateLimitError

from ai.openai_client import client
from models.ai_response import AIResponse

logger = logging.getLogger(__name__)


def generate(
    *,
    model: str,
    messages: list,
    temperature: float = 0,
    response_format=None,
) -> AIResponse:

    try:

        kwargs = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }

        if response_format:
            kwargs["response_format"] = response_format

        response = client.chat.completions.create(**kwargs)

        usage = response.usage

        logger.info(
            "LLM Call | model=%s | total_tokens=%d",
            model,
            usage.total_tokens,
        )

        return AIResponse(
            content=response.choices[0].message.content,
            model=response.model,
            prompt_tokens=usage.prompt_tokens,
            completion_tokens=usage.completion_tokens,
            total_tokens=usage.total_tokens,
            finish_reason=response.choices[0].finish_reason,
        )

    except APITimeoutError:
        logger.exception("OpenAI timeout")
        raise

    except RateLimitError:
        logger.exception("Rate limit exceeded")
        raise

    except APIError:
        logger.exception("OpenAI API error")
        raise

    except Exception:
        logger.exception("Unexpected AI error")
        raise