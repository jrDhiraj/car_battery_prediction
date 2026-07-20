import streamlit as st
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

model = load_model("battery_temp_model.h5")

# ----------------------------
# Load Objects
# ----------------------------
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("encoder.pkl")

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Battery Temperature Prediction",
    page_icon="🔋",
    layout="centered"
)

st.title("🔋 Battery Ambient Temperature Prediction")
st.write("Enter Battery Information")

# ----------------------------
# Inputs
# ----------------------------

capacity = st.number_input(
    "Capacity",
    min_value=0.0,
    value=1.67,
    format="%.6f",
    help="Example: 1.674304"
)

re = st.number_input(
    "Re",
    min_value=0.0,
    value=0.056058,
    format="%.6f",
    help="Example: 0.056058"
)

rct = st.number_input(
    "Rct",
    min_value=0.0,
    value=0.200970,
    format="%.6f",
    help="Example: 0.200970"
)

battery_type = st.selectbox(
    "Battery Type",
    ["charge", "discharge", "impedance"]
)

# ----------------------------
# Prediction
# ----------------------------

if st.button("Predict Temperature"):

    try:

        # Label Encoding
        battery_type = encoder.transform([battery_type])[0]

        # DataFrame
        df = pd.DataFrame(
            [[battery_type, capacity, re, rct]],
            columns=[
                "type",
                "Capacity",
                "Re",
                "Rct"
            ]
        )

        # Scaling
        df_scaled = scaler.transform(df)

        # Prediction
        prediction = model.predict(df_scaled, verbose=0)[0][0]

        st.success(f"🌡 Predicted Ambient Temperature : {prediction:.2f} °C")

    except Exception as e:
        st.error(str(e))