from pathlib import Path
import streamlit as st
import pandas as pd
import joblib

# =========================
# Load Model Files
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(
    BASE_DIR / "models" / "logistic_regression.pkl"
)

scaler = joblib.load(
    BASE_DIR / "models" / "scaler.pkl"
)

feature_columns = joblib.load(
    BASE_DIR / "models" / "feature_columns.pkl"
)

# =========================
# App UI
# =========================

st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="wide"
)

st.title("Customer Churn Prediction System")

st.markdown(
    "Predict whether a customer is likely to churn."
)

# =========================
# Inputs
# =========================

tenure = st.slider(
    "Tenure (Months)",
    min_value=0,
    max_value=72,
    value=12
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

senior = st.selectbox(
    "Senior Citizen",
    ["No", "Yes"]
)

partner = st.selectbox(
    "Partner",
    ["No", "Yes"]
)

avg_monthly_spend = total_charges / (tenure + 1)

# =========================
# Prediction
# =========================

if st.button("Predict Churn"):

    # Create all 31 columns
    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=feature_columns
    )

    # Numerical Features
    input_data["tenure"] = tenure
    input_data["MonthlyCharges"] = monthly_charges
    input_data["TotalCharges"] = total_charges
    input_data["AvgMonthlySpend"] = avg_monthly_spend

    # Encoded Features
    if gender == "Male":
        input_data["gender_Male"] = 1

    if senior == "Yes":
        input_data["SeniorCitizen_1"] = 1

    if partner == "Yes":
        input_data["Partner_Yes"] = 1

    # Scale
    scaled_input = scaler.transform(input_data)

    # Predict
    prediction = model.predict(
        scaled_input
    )[0]

    probability = model.predict_proba(
        scaled_input
    )[0][1]

    st.subheader(
        f"Churn Probability: {probability:.2%}"
    )

    if prediction == 1:
        st.error(
            "⚠️ Customer is likely to churn"
        )
    else:
        st.success(
            "✅ Customer is likely to stay"
        )

    st.write("Input Features Used")
    st.dataframe(input_data)