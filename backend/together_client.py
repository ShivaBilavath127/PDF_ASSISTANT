import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHERAI_API_KEY")
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"

if not TOGETHER_API_KEY:
    raise EnvironmentError("Together AI key not found. Please put it in a .env file as TOGETHERAI_API_KEY.")

def chat_with_pdf(messages):
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
    "model": "mistralai/Mistral-7B-Instruct-v0.1",  # ✅ serverless model
    "messages": messages,
    "temperature": 0.7
    }
    response = requests.post(TOGETHER_API_URL, json=payload, headers=headers)
    if response.status_code != 200:
        return f"❌ Unable to reach Together AI: {response.status_code} - {response.text}"
    return response.json()["choices"][0]["message"]["content"]
