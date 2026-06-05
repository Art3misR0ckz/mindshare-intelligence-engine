from backend.services.youtube_service import search_youtube

results = search_youtube("protein snacks")

for video in results:
    print(video)