import requests
import streamlit as st

from config.load_env import get_env
from constants.prediction_constant import (
    AgencyType,
    AgencyCategory,
    Channel,
    ProductName,
    Destination,
)
from services.prediction_service import PredictionService

env = get_env()

prediction_service = PredictionService(
    env.getenv("API_SERVICE"),
    env.getenv("AUTH_TOKEN"),
)

st.set_page_config(
    page_title="Travel Insurance Claims Prediction",
    layout="wide",
    initial_sidebar_state="expanded",
)


def build_payload():
    with st.form("prediction_form"):

        st.subheader("Travel Information")

        left, right = st.columns(2)

        with left:
            agency = st.selectbox("Agency", AgencyType)
            agency_type = st.selectbox("Agency Type", AgencyCategory)
            distribution_channel = st.selectbox(
                "Distribution Channel",
                Channel,
            )
            product_name = st.selectbox(
                "Product Name",
                ProductName,
            )

        with right:
            destination = st.selectbox(
                "Destination",
                Destination,
            )

            duration = st.number_input(
                "Duration (Days)",
                min_value=1,
                value=2,
            )

            net_sales = st.number_input(
                "Net Sales",
                value=100.0,
                step=1.0,
            )

            commission = st.number_input(
                "Commission",
                min_value=0.0,
                value=20.0,
                step=1.0,
            )

            age = st.number_input(
                "Age",
                min_value=0,
                max_value=120,
                value=22,
            )

        submitted = st.form_submit_button(
            "Predict",
            use_container_width=True,
        )

    if not submitted:
        return None

    return {
        "agency": agency,
        "agency_type": agency_type,
        "distribution_channel": distribution_channel,
        "product_name": product_name,
        "destination": destination,
        "duration": duration,
        "net_sales": float(net_sales),
        "commission": float(commission),
        "age": age,
    }


st.title("Travel Insurance Claim Prediction")

payload = build_payload()

if payload:

    with st.spinner("Predicting..."):

        try:
            status, data = prediction_service.create_prediction(payload)

            if status == 200:
                st.success(data["message"])
            else:
                st.error(data["message"])

            result = data["data"]

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Prediction ID",
                    result["id"],
                )

            with col2:
                st.metric(
                    "Prediction",
                    "Claim" if result["prediction_class"] == 1 else "No Claim",
                )

            with col3:
                st.metric(
                    "Probability",
                    f"{result['prediction_probability']:.2%}",
                )

            st.divider()

            st.subheader("Prediction Details")
            st.json(result)
        except requests.RequestException as e:
            st.error(f"Unable to connect to API.\n\n{e}")