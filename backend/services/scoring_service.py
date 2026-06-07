def calculate_trend_score(trends, youtube_results):

    if not trends:
        return {
            "trend_score": 0,
            "saturation_level": "Unknown",
            "campaign_opportunity": "Unknown"
        }

    trend_scores = [
        item["score"]
        for item in trends
    ]

    trend_avg = (
        sum(trend_scores) / len(trend_scores)
    )

    youtube_volume = len(youtube_results)

    score = 0

    # -----------------------------------
    # GOOGLE TRENDS CONTRIBUTION
    # -----------------------------------

    if trend_avg > 70:
        score += 50

    elif trend_avg > 40:
        score += 35

    else:
        score += 20

    # -----------------------------------
    # YOUTUBE SATURATION
    # -----------------------------------

    if youtube_volume < 5:

        score += 30
        saturation = "Low"

    elif youtube_volume < 15:

        score += 20
        saturation = "Medium"

    else:

        score += 10
        saturation = "High"

    # -----------------------------------
    # FINAL OPPORTUNITY
    # -----------------------------------

    if score >= 70:
        opportunity = "Strong"

    elif score >= 50:
        opportunity = "Moderate"

    else:
        opportunity = "Weak"

    return {
        "trend_score": score,
        "saturation_level": saturation,
        "campaign_opportunity": opportunity
    }