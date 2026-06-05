from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build("youtube", "v3", developerKey=API_KEY)

def search_youtube(keyword, max_results=5):
    request = youtube.search().list(
        q=keyword,
        part="snippet",
        maxResults=max_results,
        type="video"
    )

    response = request.execute()

    videos = []

    for item in response["items"]:
        videos.append({
            "title": item["snippet"]["title"],
            "channel": item["snippet"]["channelTitle"],
            "published_at": item["snippet"]["publishedAt"]
        })

    return videos