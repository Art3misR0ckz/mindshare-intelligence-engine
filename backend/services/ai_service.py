from openai import OpenAI
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------
# OPENROUTER CLIENT
# ---------------------------------------------------

client = OpenAI(

    api_key=os.getenv("OPENROUTER_API_KEY"),

    base_url="https://openrouter.ai/api/v1"
)

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

# ---------------------------------------------------
# BRAND AUDIT AI ANALYSIS
# ---------------------------------------------------

def generate_brand_audit_insights(
    brand_data
):

    prompt = f"""

You are an expert brand strategist and market analyst.

Analyze the following website data.

Identify:

1. Target audience
2. Brand tone
3. Brand positioning
4. Customer type
5. Pricing perception
6. Market maturity
7. Brand strengths
8. Suggested marketing direction

Website Data:

Title:
{brand_data['title']}

Meta Description:
{brand_data['meta_description']}

Headings:
{brand_data['headings']}

Paragraphs:
{brand_data['paragraphs']}

"""

    try:

        response = client.chat.completions.create(

            model="deepseek/deepseek-chat",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:

        print("Brand Audit AI Error:")
        print(e)

        return "Unable to generate brand audit insights."