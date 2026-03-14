import streamlit as st
import pandas as pd
import joblib

# Load trained model
import os
model_path = os.path.join(os.path.dirname(__file__), "../models/churn_model.pkl")
model = joblib.load(model_path)

st.title("Customer Churn Prediction")

st.write("Enter customer details to predict if they will churn.")

# Input features
tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)
monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=1000.0, value=70.0)
total_charges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=1000.0)

# Create input DataFrame
input_data = pd.DataFrame({
    "tenure": [tenure],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges]
})

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("Customer is likely to CHURN 🔥")
    else:
        st.success("Customer is likely to STAY ✅")