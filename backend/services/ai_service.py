from openai import OpenAI
import requests
import os

from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------
# OPENROUTER CLIENT
# ---------------------------------------------------

client = OpenAI(

    api_key=os.getenv(
        "OPENROUTER_API_KEY"
    ),

    base_url=
    "https://openrouter.ai/api/v1"
)

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)

# ---------------------------------------------------
# GENERATE MARKET INSIGHTS
# ---------------------------------------------------

def generate_insights(

    keyword,

    trends,

    youtube_results,

    market_news,

    search_results
):

    prompt = f"""

You are an advanced AI marketing intelligence strategist.

Analyze the following market attention signals.

# KEYWORD
{keyword}

# GOOGLE TRENDS DATA
{trends}

# YOUTUBE AUDIENCE SIGNALS
{youtube_results}

# MARKET NEWS
{market_news}

# GOOGLE SEARCH INTELLIGENCE
{search_results}

Generate a highly strategic marketing intelligence report.

Include:

1. Main audience interest
2. Emerging narrative
3. Suggested campaign angle
4. Market stage
   (early-stage / growth / saturated)

5. Consumer psychology
6. Hidden market opportunities
7. Content opportunities
8. Competitor positioning insights
9. Suggested short-form content strategy
10. Suggested brand positioning strategy

Be highly analytical and business-oriented.

"""

    try:

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
                ],

                "temperature": 0.7
            }
        )

        result = response.json()

        return result[
            "choices"
        ][0][
            "message"
        ][
            "content"
        ]

    except Exception as e:

        print("AI Insights Error:")
        print(e)

        return (
            "Unable to generate "
            "AI insights."
        )

# ---------------------------------------------------
# BRAND AUDIT AI ANALYSIS
# ---------------------------------------------------

def generate_brand_audit_insights(
    brand_data
):

    prompt = f"""

You are an expert brand strategist,
consumer psychologist,
and market analyst.

Analyze the following website data.

Identify:

1. Target audience
2. Brand tone
3. Brand positioning
4. Customer type
5. Pricing perception
6. Market maturity
7. Brand strengths
8. Weaknesses
9. Emotional branding strategy
10. Suggested marketing direction
11. Growth opportunities
12. Competitive positioning

# WEBSITE DATA

## Title
{brand_data['title']}

## Meta Description
{brand_data['meta_description']}

## Headings
{brand_data['headings']}

## Paragraphs
{brand_data['paragraphs']}

Generate detailed strategic insights.

"""

    try:

        response = client.chat.completions.create(

            model=
            "deepseek/deepseek-chat",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.7
        )

        return response.choices[
            0
        ].message.content

    except Exception as e:

        print("Brand Audit AI Error:")
        print(e)

        return (
            "Unable to generate "
            "brand audit insights."
        )