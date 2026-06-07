import streamlit as st
import requests
import pandas as pd

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Mindshare Intelligence Engine",
    layout="wide"
)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    ["Analyze", "History"]
)

# ---------------------------------------------------
# ANALYZE PAGE
# ---------------------------------------------------

if page == "Analyze":

    st.title("Mindshare Intelligence Engine")

    st.markdown(
        "AI-powered audience attention and campaign intelligence system"
    )

    keyword = st.text_input(
        "Enter a category or trend"
    )

    if st.button("Analyze"):

        with st.spinner(
            "Analyzing mindshare signals..."
        ):

            try:

                url = (
                    f"http://127.0.0.1:8000/analyze?keyword={keyword}"
                )

                response = requests.get(url)

                data = response.json()

                st.divider()

                # -----------------------------------------
                # SCORE CARDS
                # -----------------------------------------

                st.subheader("Opportunity Scores")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Trend Score",
                        data["scores"]["trend_score"]
                    )

                with col2:
                    st.metric(
                        "Saturation Level",
                        data["scores"]["saturation_level"]
                    )

                with col3:
                    st.metric(
                        "Campaign Opportunity",
                        data["scores"]["campaign_opportunity"]
                    )

                st.divider()

                # -----------------------------------------
                # GOOGLE TRENDS
                # -----------------------------------------

                st.subheader(
                    "Google Trends Analytics"
                )

                trends_df = pd.DataFrame(
                    data["google_trends"]
                )

                trends_df = trends_df.set_index(
                    "date"
                )

                st.line_chart(trends_df)

                latest_score = (
                    trends_df["score"].iloc[-1]
                )

                previous_score = (
                    trends_df["score"].iloc[-2]
                )

                delta = (
                    latest_score - previous_score
                )

                st.metric(
                    "Trend Momentum",
                    latest_score,
                    delta
                )

                st.divider()

                # -----------------------------------------
                # SENTIMENT ANALYSIS
                # -----------------------------------------

                st.subheader(
                    "Audience Sentiment Analysis"
                )

                sentiment = data["sentiment"]

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Positive %",
                        sentiment["positive"]
                    )

                with col2:
                    st.metric(
                        "Negative %",
                        sentiment["negative"]
                    )

                with col3:
                    st.metric(
                        "Neutral %",
                        sentiment["neutral"]
                    )

                sentiment_df = pd.DataFrame({
                    "Sentiment": [
                        "Positive",
                        "Negative",
                        "Neutral"
                    ],
                    "Percentage": [
                        sentiment["positive"],
                        sentiment["negative"],
                        sentiment["neutral"]
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
                # AI INSIGHTS
                # -----------------------------------------

                st.subheader(
                    "AI Campaign Insights"
                )

                st.success(
                    data["ai_insights"]
                )

            except Exception as e:

                st.error(f"Error: {e}")

# ---------------------------------------------------
# HISTORY PAGE
# ---------------------------------------------------

elif page == "History":

    st.title("Analysis History")

    # -----------------------------------------
    # DELETE BUTTON
    # -----------------------------------------

    if st.button("Delete All History"):

        delete_response = requests.delete(
            "http://127.0.0.1:8000/delete-history"
        )

        st.success(
            delete_response.json()["message"]
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

        for item in reversed(history_data):

            st.markdown(
                f"## {item['keyword']}"
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

        st.error(f"History Error: {e}")