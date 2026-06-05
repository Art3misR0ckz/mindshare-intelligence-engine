import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_insights(keyword, trends, youtube_results):

    prompt = f"""
    You are a marketing intelligence AI.

    Analyze the following audience attention signals.

    Keyword:
    {keyword}

    Google Trends Data:
    {trends}

    YouTube Results:
    {youtube_results}

    Give:
    1. Main audience interest
    2. Emerging narrative
    3. Suggested campaign angle
    4. Whether this looks early-stage or saturated
    """

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek/deepseek-chat",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    result = response.json()

    return result["choices"][0]["message"]["content"]
