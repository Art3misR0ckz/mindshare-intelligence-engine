from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(youtube_results):

    all_comments = []

    # -----------------------------------------
    # EXTRACT COMMENTS
    # -----------------------------------------

    for video in youtube_results:

        comments = video.get("comments", [])

        all_comments.extend(comments)

    # -----------------------------------------
    # HANDLE EMPTY COMMENTS
    # -----------------------------------------

    if not all_comments:

        return {
            "positive": 0,
            "negative": 0,
            "neutral": 0
        }

    # -----------------------------------------
    # ANALYZE SENTIMENT
    # -----------------------------------------

    positive_scores = []
    negative_scores = []
    neutral_scores = []

    for comment in all_comments:

        scores = analyzer.polarity_scores(comment)

        positive_scores.append(scores["pos"])
        negative_scores.append(scores["neg"])
        neutral_scores.append(scores["neu"])

    # -----------------------------------------
    # AVERAGE SCORES
    # -----------------------------------------

    positive = (
        sum(positive_scores)
        / len(positive_scores)
    ) * 100

    negative = (
        sum(negative_scores)
        / len(negative_scores)
    ) * 100

    neutral = (
        sum(neutral_scores)
        / len(neutral_scores)
    ) * 100

    return {
        "positive": round(positive, 2),
        "negative": round(negative, 2),
        "neutral": round(neutral, 2)
    }