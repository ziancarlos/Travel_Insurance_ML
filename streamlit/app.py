import streamlit as st

st.set_page_config(
    page_title="Travel Insurance Claims Prediction",
    layout="wide",
    initial_sidebar_state="expanded",
)

predict_page = st.Page(
    "pages/predict.py",
    title="Predict",
    default=True,
)

all_predictions_page = st.Page(
    "pages/all_predictions.py",
    title="All Predictions",
)

pg = st.navigation([predict_page, all_predictions_page])
pg.run()