import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Mindshare Intelligence Engine",
    layout="wide"
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("Mindshare Intelligence Engine")

st.markdown(
    "AI-powered audience attention and campaign intelligence system"
)

# ---------------------------------------------------
# USER INPUT
# ---------------------------------------------------

keyword = st.text_input(
    "Enter a category or trend"
)

# ---------------------------------------------------
# ANALYZE BUTTON
# ---------------------------------------------------

if st.button("Analyze"):

    with st.spinner("Analyzing mindshare signals..."):

        try:

            # ---------------------------------------------------
            # API REQUEST
            # ---------------------------------------------------

            url = (
                f"http://127.0.0.1:8000/analyze?keyword={keyword}"
            )

            response = requests.get(url)

            data = response.json()

            st.divider()

            # ---------------------------------------------------
            # SCORE CARDS
            # ---------------------------------------------------

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

            # ---------------------------------------------------
            # GOOGLE TRENDS ANALYTICS
            # ---------------------------------------------------

            st.subheader("Google Trends Analytics")

            trends_df = pd.DataFrame(
                data["google_trends"]
            )

            trends_df = trends_df.set_index("date")

            st.line_chart(trends_df)

            # ---------------------------------------------------
            # TREND MOMENTUM
            # ---------------------------------------------------

            latest_score = (
                trends_df["score"].iloc[-1]
            )

            previous_score = (
                trends_df["score"].iloc[-2]
            )

            delta = latest_score - previous_score

            st.metric(
                "Trend Momentum",
                latest_score,
                delta
            )

            st.divider()

            # ---------------------------------------------------
            # YOUTUBE SIGNALS
            # ---------------------------------------------------

            st.subheader("YouTube Signals")

            for video in data["youtube_results"]:

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

            # ---------------------------------------------------
            # AI INSIGHTS
            # ---------------------------------------------------

            st.subheader("AI Campaign Insights")

            st.success(data["ai_insights"])

        except Exception as e:

            st.error(f"Error: {e}")

# ---------------------------------------------------
# HISTORY SECTION
# ---------------------------------------------------

st.divider()

st.subheader("Previous Analyses")

try:

    history_response = requests.get(
        "http://127.0.0.1:8000/history"
    )

    history_data = history_response.json()

    for item in reversed(history_data[-5:]):

        st.markdown(
            f"### {item['keyword']}"
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