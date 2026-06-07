from backend.services.youtube_service import search_youtube

results = search_youtube("protein snacks")

for video in results:

    print("\n---------------------------")
    print("TITLE:", video["title"])
    print("CHANNEL:", video["channel"])
    print("PUBLISHED:", video["published_at"])

    print("\nCOMMENTS:")

    for comment in video["comments"]:
        print("-", comment)