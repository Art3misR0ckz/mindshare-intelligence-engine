from pytrends.request import TrendReq

# ---------------------------------------------------
# INITIALIZE PYTRENDS
# ---------------------------------------------------

pytrends = TrendReq(
    hl='en-US',
    tz=330
)

# ---------------------------------------------------
# GET GOOGLE TRENDS DATA
# ---------------------------------------------------

def get_trends(
    keyword,
    location="",
    timeframe="today 12-m"
):

    """
    Fetch Google Trends data.

    Parameters:
    - keyword: search term
    - location: country code
      Example:
      IN = India
      US = United States
      GB = United Kingdom

    - timeframe:
      Examples:
      today 3-m
      today 12-m
      today 5-y
    """

    try:

        # -----------------------------------------
        # BUILD PAYLOAD
        # -----------------------------------------

        if location:

            pytrends.build_payload(
                [keyword],
                timeframe=timeframe,
                geo=location
            )

        else:

            pytrends.build_payload(
                [keyword],
                timeframe=timeframe
            )

        # -----------------------------------------
        # FETCH DATA
        # -----------------------------------------

        data = pytrends.interest_over_time()

        # -----------------------------------------
        # HANDLE EMPTY DATA
        # -----------------------------------------

        if data.empty:
            return []

        # -----------------------------------------
        # FORMAT RESULTS
        # -----------------------------------------

        results = []

        for index, row in data.iterrows():

            results.append({
                "date": str(index.date()),
                "score": int(row[keyword])
            })

        print(results[:5])
        return results

    except Exception as e:

        print("Google Trends Error:")
        print(e)

        return []