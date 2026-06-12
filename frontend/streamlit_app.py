import streamlit as st
import requests
import pandas as pd

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(

    page_title=
    "Mindshare Intelligence Engine",

    layout="wide"
)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title(
    "Navigation"
)

page = st.sidebar.radio(

    "Go To",

    [
        "Analyze",
        "Brand Audit",
        "History"
    ]
)

# ---------------------------------------------------
# ANALYZE PAGE
# ---------------------------------------------------

if page == "Analyze":

    st.title(
        "Mindshare Intelligence Engine"
    )

    st.markdown(
        """
AI-powered audience attention
and campaign intelligence system
"""
    )

    # ---------------------------------------------------
    # INPUTS
    # ---------------------------------------------------

    keyword = st.text_input(
        "Enter a category or trend"
    )

    location = st.selectbox(

        "Select Market Location",

        [
            "",
            "IN",
            "US",
            "GB",
            "CA",
            "AU"
        ]
    )

    timeframe = st.selectbox(

        "Select Trend Timeline",

        [
            "today 3-m",
            "today 12-m",
            "today 5-y"
        ]
    )

    # ---------------------------------------------------
    # ANALYZE BUTTON
    # ---------------------------------------------------

    if st.button("Analyze"):

        with st.spinner(
            "Analyzing mindshare signals..."
        ):

            try:

                # -----------------------------------------
                # API CALL
                # -----------------------------------------

                response = requests.get(

                    "http://127.0.0.1:8000/analyze",

                    params={

                        "keyword":
                        keyword,

                        "location":
                        location,

                        "timeframe":
                        timeframe
                    }
                )

                data = response.json()

                st.divider()

                # -----------------------------------------
                # SCORE CARDS
                # -----------------------------------------

                st.subheader(
                    "Opportunity Scores"
                )

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(

                        "Trend Score",

                        data["scores"][
                            "trend_score"
                        ]
                    )

                with col2:

                    st.metric(

                        "Saturation Level",

                        data["scores"][
                            "saturation_level"
                        ]
                    )

                with col3:

                    st.metric(

                        "Campaign Opportunity",

                        data["scores"][
                            "campaign_opportunity"
                        ]
                    )

                st.divider()

                # -----------------------------------------
                # GOOGLE TRENDS
                # -----------------------------------------

                st.subheader(
                    "Google Trends Analytics"
                )

                trends_data = data[
                    "google_trends"
                ]

                if not trends_data:

                    st.warning(
                        "No Google Trends data found."
                    )

                else:

                    trends_df = pd.DataFrame(
                        trends_data
                    )

                    trends_df = trends_df.set_index(
                        "date"
                    )

                    st.line_chart(
                        trends_df
                    )

                    latest_score = (
                        trends_df[
                            "score"
                        ].iloc[-1]
                    )

                    previous_score = (
                        trends_df[
                            "score"
                        ].iloc[-2]
                    )

                    delta = (
                        latest_score -
                        previous_score
                    )

                    st.metric(

                        "Trend Momentum",

                        latest_score,

                        delta
                    )

                st.divider()

                # -----------------------------------------
                # SEARCH INTELLIGENCE
                # -----------------------------------------

                st.subheader(
                    "Search Intelligence"
                )

                search_results = data[
                    "search_results"
                ]

                if not search_results:

                    st.warning(
                        "No search intelligence found."
                    )

                else:

                    for result in search_results[:5]:

                        st.markdown(
                            f"### {result['title']}"
                        )

                        st.write(
                            result["snippet"]
                        )

                        st.write(
                            result["link"]
                        )

                        st.divider()

                # -----------------------------------------
                # MARKET NEWS
                # -----------------------------------------

                st.subheader(
                    "Market Intelligence News"
                )

                market_news = data[
                    "market_news"
                ]

                if not market_news:

                    st.warning(
                        "No market news found."
                    )

                else:

                    for article in market_news:

                        st.markdown(
                            f"### {article['title']}"
                        )

                        st.write(
                            f"Source: {article['source']}"
                        )

                        st.write(
                            article[
                                "description"
                            ]
                        )

                        st.write(
                            article[
                                "published_at"
                            ]
                        )

                        st.write(
                            article["url"]
                        )

                        st.divider()

                # -----------------------------------------
                # SENTIMENT ANALYSIS
                # -----------------------------------------

                st.subheader(
                    "Audience Sentiment Analysis"
                )

                sentiment = data[
                    "sentiment"
                ]

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(

                        "Positive %",

                        sentiment[
                            "positive"
                        ]
                    )

                with col2:

                    st.metric(

                        "Negative %",

                        sentiment[
                            "negative"
                        ]
                    )

                with col3:

                    st.metric(

                        "Neutral %",

                        sentiment[
                            "neutral"
                        ]
                    )

                sentiment_df = pd.DataFrame({

                    "Sentiment": [

                        "Positive",

                        "Negative",

                        "Neutral"
                    ],

                    "Percentage": [

                        sentiment[
                            "positive"
                        ],

                        sentiment[
                            "negative"
                        ],

                        sentiment[
                            "neutral"
                        ]
                    ]
                })

                st.bar_chart(

                    sentiment_df.set_index(
                        "Sentiment"
                    )
                )

                st.divider()

                # -----------------------------------------
                # YOUTUBE RESULTS
                # -----------------------------------------

                st.subheader(
                    "YouTube Signals"
                )

                for video in data[
                    "youtube_results"
                ]:

                    st.markdown(
                        f"### {video['title']}"
                    )

                    st.write(
                        f"Channel: {video['channel']}"
                    )

                    st.write(
                        f"Published: {video['published_at']}"
                    )

                    st.divider()

                # -----------------------------------------
                # COMMENT INSIGHTS
                # -----------------------------------------

                st.subheader(
                    "Audience Comment Insights"
                )

                st.info(
                    data["comment_insights"]
                )

                st.divider()

                # -----------------------------------------
                # CUSTOMER PERSONA
                # -----------------------------------------

                st.subheader(
                    "Customer Persona Intelligence"
                )

                persona = data[
                    "customer_persona"
                ]

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(

                        "Primary Age Group",

                        persona[
                            "age_group"
                        ]
                    )

                    st.write(
                        "### Lifestyle"
                    )

                    st.write(
                        persona[
                            "lifestyle"
                        ]
                    )

                    st.write(
                        "### Interests"
                    )

                    st.write(
                        persona[
                            "interests"
                        ]
                    )

                    st.write(
                        "### Buying Behavior"
                    )

                    st.write(
                        persona[
                            "buying_behavior"
                        ]
                    )

                with col2:

                    st.write(
                        "### Emotional Triggers"
                    )

                    st.write(
                        persona[
                            "emotional_triggers"
                        ]
                    )

                    st.write(
                        "### Platform Preferences"
                    )

                    st.write(
                        persona[
                            "platform_preferences"
                        ]
                    )

                    st.write(
                        "### Consumer Motivations"
                    )

                    st.write(
                        persona[
                            "consumer_motivations"
                        ]
                    )

                    st.write(
                        "### Pain Points"
                    )

                    st.write(
                        persona[
                            "pain_points"
                        ]
                    )

                st.divider()

                st.subheader(
                    "Customer Archetype"
                )

                st.success(

                    persona[
                        "customer_archetype"
                    ]
                )

                st.divider()

                st.subheader(
                    "Marketing Recommendations"
                )

                st.info(

                    persona[
                        "marketing_recommendations"
                    ]
                )

                st.divider()

                # -----------------------------------------
                # AI INSIGHTS
                # -----------------------------------------

                st.subheader(
                    "AI Campaign Insights"
                )

                st.success(
                    data["ai_insights"]
                )

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )

# ---------------------------------------------------
# BRAND AUDIT PAGE
# ---------------------------------------------------

elif page == "Brand Audit":

    st.title(
        "AI Brand Audit"
    )

    st.markdown(
        """
Analyze a brand website using
AI-powered market positioning
intelligence.
"""
    )

    website_url = st.text_input(
        "Enter Brand Website URL"
    )

    if st.button(
        "Run Brand Audit"
    ):

        with st.spinner(
            "Analyzing brand positioning..."
        ):

            try:

                response = requests.get(

                    "http://127.0.0.1:8000/brand-audit",

                    params={
                        "url":
                        website_url
                    }
                )

                data = response.json()

                st.divider()

                # ---------------------------------
                # WEBSITE DATA
                # ---------------------------------

                st.subheader(
                    "Website Intelligence"
                )

                website_data = data[
                    "website_data"
                ]

                st.write(
                    f"### {website_data['title']}"
                )

                st.info(
                    website_data[
                        "meta_description"
                    ]
                )

                st.divider()

                # ---------------------------------
                # HEADINGS
                # ---------------------------------

                st.subheader(
                    "Brand Messaging"
                )

                for heading in website_data[
                    "headings"
                ][:10]:

                    st.write(
                        f"• {heading}"
                    )

                st.divider()

                # ---------------------------------
                # CUSTOMER PERSONA
                # ---------------------------------

                st.subheader(
                    "Customer Persona Intelligence"
                )

                persona = data[
                    "customer_persona"
                ]

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(

                        "Primary Age Group",

                        persona[
                            "age_group"
                        ]
                    )

                    st.write(
                        "### Lifestyle"
                    )

                    st.write(
                        persona[
                            "lifestyle"
                        ]
                    )

                    st.write(
                        "### Interests"
                    )

                    st.write(
                        persona[
                            "interests"
                        ]
                    )

                    st.write(
                        "### Buying Behavior"
                    )

                    st.write(
                        persona[
                            "buying_behavior"
                        ]
                    )

                with col2:

                    st.write(
                        "### Emotional Triggers"
                    )

                    st.write(
                        persona[
                            "emotional_triggers"
                        ]
                    )

                    st.write(
                        "### Platform Preferences"
                    )

                    st.write(
                        persona[
                            "platform_preferences"
                        ]
                    )

                    st.write(
                        "### Consumer Motivations"
                    )

                    st.write(
                        persona[
                            "consumer_motivations"
                        ]
                    )

                    st.write(
                        "### Pain Points"
                    )

                    st.write(
                        persona[
                            "pain_points"
                        ]
                    )

                st.divider()

                st.subheader(
                    "Customer Archetype"
                )

                st.success(

                    persona[
                        "customer_archetype"
                    ]
                )

                st.divider()

                st.subheader(
                    "Marketing Recommendations"
                )

                st.info(

                    persona[
                        "marketing_recommendations"
                    ]
                )

                st.divider()

                # ---------------------------------
                # AI INSIGHTS
                # ---------------------------------

                st.subheader(
                    "AI Brand Intelligence"
                )

                st.success(
                    data[
                        "brand_insights"
                    ]
                )

            except Exception as e:

                st.error(
                    f"Brand Audit Error: {e}"
                )

# ---------------------------------------------------
# HISTORY PAGE
# ---------------------------------------------------

elif page == "History":

    st.title(
        "Analysis History"
    )

    if st.button(
        "Delete All History"
    ):

        delete_response = requests.delete(

            "http://127.0.0.1:8000/delete-history"
        )

        st.success(
            delete_response.json()[
                "message"
            ]
        )

    st.divider()

    try:

        history_response = requests.get(
            "http://127.0.0.1:8000/history"
        )

        history_data = history_response.json()

        if not history_data:

            st.warning(
                "No saved analyses found."
            )

        for item in reversed(
            history_data
        ):

            st.markdown(
                f"## {item['keyword']}"
            )

            st.write(
                f"Location: {item.get('location', '')}"
            )

            st.write(
                f"Timeframe: {item.get('timeframe', '')}"
            )

            st.write(
                f"Trend Score: {item['scores']['trend_score']}"
            )

            st.write(
                f"Opportunity: {item['scores']['campaign_opportunity']}"
            )

            st.write(
                item["ai_insights"]
            )

            st.divider()

    except Exception as e:

        st.error(
            f"History Error: {e}"
        )