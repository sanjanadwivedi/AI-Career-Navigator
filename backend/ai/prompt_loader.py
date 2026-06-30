from functools import lru_cache
from pathlib import Path
import logging

from config import PROMPT_LABEL
from ai.langfuse_client import langfuse

logger = logging.getLogger(__name__)

PROMPTS_DIR = Path(__file__).parent / "prompts"


@lru_cache(maxsize=20)
def _load_prompt(name: str, label: str):
    return langfuse.get_prompt(
        name=name,
        label=label,
    )


def _load_local_prompt(name: str) -> str:
    prompt_file = PROMPTS_DIR / f"{name}.txt"

    if not prompt_file.exists():
        raise FileNotFoundError(f"Local prompt not found: {prompt_file}")

    return prompt_file.read_text(encoding="utf-8")


def get_prompt(name: str, **variables) -> str:
    try:
        prompt = _load_prompt(name, PROMPT_LABEL)

        print("✅ Prompt loaded from Langfuse")

        return prompt.compile(**variables)

    except Exception:
        print("⚠️ Using local fallback prompt")

        logger.exception(
            "Failed to load Langfuse prompt '%s' (label=%s). Falling back to local prompt.",
            name,
            PROMPT_LABEL,
        )

        local_prompt = _load_local_prompt(name)
        return local_prompt.format(**variables)