from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(youtube_results):

    sentiments = []

    for video in youtube_results:

        text = video["title"]

        score = analyzer.polarity_scores(text)

        sentiments.append(score)

    if not sentiments:

        return {
            "positive": 0,
            "negative": 0,
            "neutral": 0
        }

    positive = sum(
        s["pos"] for s in sentiments
    ) / len(sentiments)

    negative = sum(
        s["neg"] for s in sentiments
    ) / len(sentiments)

    neutral = sum(
        s["neu"] for s in sentiments
    ) / len(sentiments)

    return {
        "positive": round(positive * 100, 2),
        "negative": round(negative * 100, 2),
        "neutral": round(neutral * 100, 2)
    }