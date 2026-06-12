import requests
import os

from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv(
    "NEWS_API_KEY"
)

# ---------------------------------------------------
# FETCH MARKET NEWS
# ---------------------------------------------------

def get_market_news(keyword):

    results = []

    try:

        url = (
            "https://newsapi.org/v2/everything"
        )

        params = {

            "q": keyword,

            "language": "en",

            "sortBy": "publishedAt",

            "pageSize": 5,

            "apiKey": NEWS_API_KEY
        }

        response = requests.get(
            url,
            params=params
        )

        data = response.json()

        articles = data["articles"]

        for article in articles:

            results.append({

                "title":
                article["title"],

                "source":
                article["source"]["name"],

                "description":
                article["description"],

                "url":
                article["url"],

                "published_at":
                article["publishedAt"]
            })

        return results

    except Exception as e:

        print("News API Error:")
        print(e)

        return []