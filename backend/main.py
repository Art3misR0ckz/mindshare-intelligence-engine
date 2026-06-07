from backend.services.ai_service import generate_insights
from backend.services.scoring_service import calculate_trend_score
from fastapi import FastAPI
from backend.services.google_trends import get_trends
from backend.services.youtube_service import search_youtube
from backend.services.db_service import analysis_collection
from backend.services.sentiment_service import analyze_sentiment
from backend.services.comment_insight_service import generate_comment_insights

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Mindshare Intelligence Engine Running"}

@app.get("/analyze")
def analyze(keyword: str):

    trends = get_trends(keyword)

    youtube_results = search_youtube(keyword)
    sentiment=analyze_sentiment(youtube_results)
    comment_insights = generate_comment_insights(youtube_results)
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
        "comment_insights": comment_insights,
        "scores": scores,
        "ai_insights": insights
    }

    analysis_collection.insert_one(analysis_document)

    return {
        "keyword": keyword,
        "google_trends": trends,
        "youtube_results": youtube_results,
        "sentiment": sentiment,
        "comment_insights": comment_insights,
        "scores": scores,
        "ai_insights": insights
        
    }

@app.get("/history")
def get_history():

    history = list(
        analysis_collection.find({}, {"_id": 0})
    )

    return history

@app.delete("/delete-history")
def delete_history():

    analysis_collection.delete_many({})

    return {
        "message": "History deleted successfully"
    }
