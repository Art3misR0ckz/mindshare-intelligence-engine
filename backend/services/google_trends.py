from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=330)

def get_trends(keyword):
    pytrends.build_payload([keyword], timeframe='today 3-m')
    
    data = pytrends.interest_over_time()
    
    if data.empty:
        return None
    
    return data[keyword].tail(10).tolist()