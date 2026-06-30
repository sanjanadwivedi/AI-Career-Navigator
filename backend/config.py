import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI Models
OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-4.1"
)

EVALUATION_MODEL = os.getenv(
    "EVALUATION_MODEL",
    "gpt-4.1-mini"
)

# Langfuse
PROMPT_LABEL = os.getenv(
    "PROMPT_LABEL",
    "production"
)