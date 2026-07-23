import requests
import pandas as pd
import streamlit as st

from config.load_env import get_env
from services.prediction_service import PredictionService

env = get_env()

prediction_service = PredictionService(
    env.getenv("API_SERVICE"),
    env.getenv("AUTH_TOKEN"),
)

st.title("All Predictions")

if st.button("Refresh"):
    st.rerun()

with st.spinner("Loading predictions..."):
    try:
        status, data = prediction_service.get_predictions()

        if status != 200:
            st.error(data.get("message", "Failed to fetch predictions."))
        else:
            results = data.get("data", [])

            if not results:
                st.info("No predictions found.")
            else:
                st.caption(f"{len(results)} prediction(s) found")

                df = pd.DataFrame(results)

                if "prediction_class" in df.columns:
                    df["prediction_class"] = df["prediction_class"].map(
                        {0: "Not Claim", 1: "Claim"}
                    )

                df.columns = [
                    col.replace("_", " ").title() for col in df.columns
                ]
                
                df.sort_values("Id", ascending=False, inplace=True)

                st.dataframe(df, use_container_width=True, hide_index=True)

                st.divider()
                st.subheader("Raw Data")
                st.json(results)

    except requests.RequestException as e:
        st.error(f"Unable to connect to API.\n\n{e}")