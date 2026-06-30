import os
from dotenv import load_dotenv

from langfuse.openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)