from fastapi import FastAPI

from backend.services.google_trends import get_trends
from backend.services.youtube_service import search_youtube
from backend.services.sentiment_service import analyze_sentiment
from backend.services.comment_insight_service import generate_comment_insights
from backend.services.scoring_service import calculate_trend_score
from backend.services.ai_service import generate_insights
from backend.services.db_service import analysis_collection
from backend.services.brand_audit_service import audit_brand_website

from backend.services.ai_service import generate_brand_audit_insights
from backend.services.persona_service import (generate_customer_persona)

# ---------------------------------------------------
# FASTAPI INITIALIZATION
# ---------------------------------------------------

app = FastAPI()

# ---------------------------------------------------
# HOME ROUTE
# ---------------------------------------------------

@app.get("/")
def home():

    return {
        "message":
        "Mindshare Intelligence Engine Running"
    }

# ---------------------------------------------------
# ANALYZE ROUTE
# ---------------------------------------------------

@app.get("/analyze")
def analyze(
    keyword: str,
    location: str = "",
    timeframe: str = "today 12-m"
):

    # -----------------------------------------
    # GOOGLE TRENDS
    # -----------------------------------------

    trends = get_trends(
        keyword,
        location,
        timeframe
    )

    # -----------------------------------------
    # YOUTUBE DATA
    # -----------------------------------------

    youtube_results = search_youtube(
        keyword
    )

    # -----------------------------------------
    # SENTIMENT ANALYSIS
    # -----------------------------------------

    sentiment = analyze_sentiment(
        youtube_results
    )

    # -----------------------------------------
    # COMMENT INSIGHTS
    # -----------------------------------------

    comment_insights = (
        generate_comment_insights(
            youtube_results
        )
    )

    # -----------------------------------------
    # SCORING ENGINE
    # -----------------------------------------

    scores = calculate_trend_score(
        trends,
        youtube_results
    )

    # -----------------------------------------
    # AI STRATEGIC INSIGHTS
    # -----------------------------------------

    insights = generate_insights(
        keyword,
        trends,
        youtube_results
    )


    persona = generate_customer_persona(
        keyword,
        sentiment,
        comment_insights,
        insights
    )

    # -----------------------------------------
    # MONGODB DOCUMENT
    # -----------------------------------------

    analysis_document = {

        "keyword": keyword,

        "location": location,

        "timeframe": timeframe,

        "google_trends": trends,

        "youtube_results": youtube_results,

        "sentiment": sentiment,

        "customer_persona": persona,

        "comment_insights": comment_insights,

        "scores": scores,

        "ai_insights": insights
    }

    # -----------------------------------------
    # SAVE TO MONGODB
    # -----------------------------------------

    analysis_collection.insert_one(
        analysis_document
    )

    # -----------------------------------------
    # API RESPONSE
    # -----------------------------------------

    return {

        "keyword": keyword,

        "location": location,

        "timeframe": timeframe,

        "google_trends": trends,

        "youtube_results": youtube_results,

        "sentiment": sentiment,

        "customer_persona": persona,

        "comment_insights": comment_insights,

        "scores": scores,

        "ai_insights": insights
    }

# ---------------------------------------------------
# BRAND AUDIT ENDPOINT
# ---------------------------------------------------

@app.get("/brand-audit")
def brand_audit(url: str):

    # -----------------------------------------
    # SCRAPE WEBSITE
    # -----------------------------------------

    brand_data = audit_brand_website(
        url
    )

    # -----------------------------------------
    # AI ANALYSIS
    # -----------------------------------------

    insights = (
        generate_brand_audit_insights(
            brand_data
        )
    )

    return {

        "website_data": brand_data,

        "brand_insights": insights
    }



# ---------------------------------------------------
# HISTORY ROUTE
# ---------------------------------------------------

@app.get("/history")
def get_history():

    history = list(
        analysis_collection.find(
            {},
            {"_id": 0}
        )
    )

    return history

# ---------------------------------------------------
# DELETE HISTORY
# ---------------------------------------------------

@app.delete("/delete-history")
def delete_history():

    analysis_collection.delete_many({})

    return {
        "message":
        "History deleted successfully"
    }