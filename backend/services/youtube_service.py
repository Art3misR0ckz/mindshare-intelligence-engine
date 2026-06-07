from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

# ---------------------------------------------------
# FETCH VIDEO COMMENTS
# ---------------------------------------------------

def get_video_comments(video_id, max_comments=15):

    try:

        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=max_comments,
            textFormat="plainText"
        )

        response = request.execute()

        comments = []

        for item in response["items"]:

            comment = item["snippet"][
                "topLevelComment"
            ]["snippet"]["textDisplay"]

            comments.append(comment)

        return comments

    except Exception as e:

        print("Comment Error:", e)

        return []

# ---------------------------------------------------
# SEARCH YOUTUBE VIDEOS
# ---------------------------------------------------

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

        video_id = item["id"]["videoId"]

        comments = get_video_comments(video_id)

        videos.append({
            "title": item["snippet"]["title"],
            "channel": item["snippet"]["channelTitle"],
            "published_at": item["snippet"]["publishedAt"],
            "comments": comments
        })

    return videos