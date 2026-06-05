def calculate_trend_score(trends, youtube_results):

    trend_avg = sum(trends) / len(trends)

    youtube_volume = len(youtube_results)

    score = 0

    # Google Trends contribution
    if trend_avg > 70:
        score += 50
    elif trend_avg > 40:
        score += 35
    else:
        score += 20

    # YouTube saturation contribution
    if youtube_volume < 5:
        score += 30
        saturation = "Low"
    elif youtube_volume < 15:
        score += 20
        saturation = "Medium"
    else:
        score += 10
        saturation = "High"

    # Final classification
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