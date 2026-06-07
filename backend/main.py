from backend.services.ai_service import generate_insights
from backend.services.scoring_service import calculate_trend_score
from fastapi import FastAPI
from backend.services.google_trends import get_trends
from backend.services.youtube_service import search_youtube
from backend.services.db_service import analysis_collection
from backend.services.sentiment_service import analyze_sentiment

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Mindshare Intelligence Engine Running"}

@app.get("/analyze")
def analyze(keyword: str):

    trends = get_trends(keyword)

    youtube_results = search_youtube(keyword)
    sentiment=analyze_sentiment(youtube_results)
    scores=calculate_trend_score(trends, youtube_results)

    insights = generate_insights(
        keyword,
        trends,
        youtube_results
    )

    

    analysis_document = {
        "keyword": keyword,
        "google_trends": trends,
        "youtube_results": youtube_results,
        "scores": scores,
        "ai_insights": insights
    }

    analysis_collection.insert_one(analysis_document)

    return {
        "keyword": keyword,
        "google_trends": trends,
        "youtube_results": youtube_results,
        "sentiment": sentiment,
        "scores": scores,
        "ai_insights": insights
        
    }

@app.get("/history")
def get_history():

    history = list(
        analysis_collection.find({}, {"_id": 0})
    )

    return history

