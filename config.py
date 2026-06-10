from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    "qwen/qwen3-8b",
    model_provider="openai",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPEN_ROUTER"),
)