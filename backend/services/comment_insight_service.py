import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)

def generate_comment_insights(youtube_results):

    all_comments = []

    # -----------------------------------------
    # COLLECT COMMENTS
    # -----------------------------------------

    for video in youtube_results:

        comments = video.get("comments", [])

        all_comments.extend(comments)

    # -----------------------------------------
    # LIMIT COMMENTS
    # -----------------------------------------

    combined_comments = "\n".join(
        all_comments[:50]
    )

    # -----------------------------------------
    # PROMPT
    # -----------------------------------------

    prompt = f"""
    Analyze these audience comments.

    Comments:
    {combined_comments}

    Identify:

    1. Common complaints
    2. Positive themes
    3. Audience desires
    4. Repeated frustrations
    5. Marketing insights

    Keep the response concise and structured.
    """

    # -----------------------------------------
    # API CALL
    # -----------------------------------------

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization":
            f"Bearer {OPENROUTER_API_KEY}",

            "Content-Type":
            "application/json"
        },
        json={
            "model":
            "deepseek/deepseek-chat",

            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    result = response.json()

    return result["choices"][0][
        "message"
    ]["content"]