from fastapi import FastAPI
from backend.services.google_trends import get_trends
from backend.services.youtube_service import search_youtube

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Mindshare Intelligence Engine Running"}

@app.get("/analyze")
def analyze(keyword: str):

    trends = get_trends(keyword)

    youtube_results = search_youtube(keyword)

    return {
        "keyword": keyword,
        "google_trends": trends,
        "youtube_results": youtube_results
    }