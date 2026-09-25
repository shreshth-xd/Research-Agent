import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    "google/gemma-4-26b-a4b-it",
    model_provider="openai",
    api_key=os.environ["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1",
    temperature=0.5,
    timeout=600,
    max_tokens=25000,
    streaming=True,
)