import json

from backend.services.ai_service import client

# ---------------------------------------------------
# CUSTOMER PERSONA GENERATOR
# ---------------------------------------------------

def generate_customer_persona(

    keyword,
    sentiment,
    comment_insights,
    brand_insights
):

    prompt = f"""

You are an expert consumer psychologist
and market intelligence strategist.

Based on the following data,
generate a structured customer persona.

Return ONLY valid JSON.

Required JSON format:

{{
    "age_group": "",
    "lifestyle": "",
    "interests": "",
    "buying_behavior": "",
    "emotional_triggers": "",
    "platform_preferences": "",
    "consumer_motivations": "",
    "pain_points": "",
    "customer_archetype": "",
    "marketing_recommendations": ""
}}

Keyword:
{keyword}

Sentiment:
{sentiment}

Comment Insights:
{comment_insights}

Brand Insights:
{brand_insights}

"""

    try:

        completion = client.chat.completions.create(

            model="openai/gpt-oss-20b",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = (
            completion
            .choices[0]
            .message
            .content
        )

        # -----------------------------------------
        # CLEAN JSON RESPONSE
        # -----------------------------------------

        content = content.strip()

        if content.startswith("```json"):
            content = (
                content
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

        persona_data = json.loads(content)

        return persona_data

    except Exception as e:

        print("Persona JSON Error:")
        print(e)

        return {
            "age_group": "Unknown",
            "lifestyle": "Unknown",
            "interests": "Unknown",
            "buying_behavior": "Unknown",
            "emotional_triggers": "Unknown",
            "platform_preferences": "Unknown",
            "consumer_motivations": "Unknown",
            "pain_points": "Unknown",
            "customer_archetype": "Unknown",
            "marketing_recommendations": "Unable to generate"
        }