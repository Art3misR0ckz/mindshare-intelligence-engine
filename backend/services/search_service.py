import os

from serpapi import GoogleSearch
from dotenv import load_dotenv

# ---------------------------------------------------
# LOAD ENV VARIABLES
# ---------------------------------------------------

load_dotenv()

SERP_API_KEY = os.getenv(
    "SERP_API_KEY"
)

# ---------------------------------------------------
# GOOGLE SEARCH INTELLIGENCE
# ---------------------------------------------------

def get_search_intelligence(
    keyword
):

    results = []

    try:

        # -----------------------------------------
        # SEARCH PARAMETERS
        # -----------------------------------------

        params = {

            "engine": "google",

            "q": keyword,

            "api_key": SERP_API_KEY,

            "num": 10,

            "google_domain":
            "google.com",

            "hl": "en",

            "gl": "us"
        }

        # -----------------------------------------
        # EXECUTE SEARCH
        # -----------------------------------------

        search = GoogleSearch(
            params
        )

        data = search.get_dict()

        # -----------------------------------------
        # ORGANIC RESULTS
        # -----------------------------------------

        organic_results = data.get(
            "organic_results",
            []
        )

        # -----------------------------------------
        # FORMAT RESULTS
        # -----------------------------------------

        for item in organic_results:

            results.append({

                "title":
                item.get(
                    "title",
                    ""
                ),

                "snippet":
                item.get(
                    "snippet",
                    ""
                ),

                "link":
                item.get(
                    "link",
                    ""
                ),

                "position":
                item.get(
                    "position",
                    ""
                )
            })

        # -----------------------------------------
        # RETURN RESULTS
        # -----------------------------------------

        return results

    except Exception as e:

        print(
            "SERP API Error:"
        )

        print(e)

        return []