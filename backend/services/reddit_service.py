import requests

# ---------------------------------------------------
# SEARCH REDDIT
# ---------------------------------------------------

def search_reddit(keyword):

    results = []

    try:

        headers = {

            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        url = (
            "https://old.reddit.com/search.json"
            f"?q={keyword}&limit=10"
        )

        response = requests.get(
            url,
            headers=headers
        )

        print(response.status_code)

        if response.status_code != 200:

            print("Reddit Request Failed")

            return []

        data = response.json()

        posts = data["data"]["children"]

        for post in posts:

            p = post["data"]

            results.append({

                "title":
                p["title"],

                "subreddit":
                p["subreddit"],

                "content":
                p.get("selftext", ""),

                "score":
                p["score"],

                "comments":
                p["num_comments"],

                "url":
                "https://reddit.com"
                + p["permalink"]

            })

        return results

    except Exception as e:

        print("Reddit Error:")
        print(e)

        return []