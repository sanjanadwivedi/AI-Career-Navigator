from dataclasses import dataclass
from typing import Optional


@dataclass
class AIResponse:
    content: str
    model: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    finish_reason: Optional[str]