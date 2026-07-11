import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ---------------------------
# Load your trained model
# ---------------------------
rf_model = joblib.load("fraud_model.pkl")   # save your model first (I’ll show below)

# ---------------------------
# App Title
# ---------------------------
st.title("💳 Fraud Detection System")

st.write("Enter transaction details or use sample data")

# ---------------------------
# Load sample data (for testing)
# ---------------------------
data = pd.read_csv("processed_data.csv")  # your dataset

# ---------------------------
# Option 1: Use random sample
# ---------------------------
if st.button("🔄 Use Random Sample"):
    sample = data.sample(1)
    st.write("Sample Input:", sample)

    prob = rf_model.predict_proba(sample)[0][1]

    if prob > 0.7:
        st.error(f"🚨 Fraud Detected!high risk transation... Risk Score: {prob:.4f}")
    elif prob > 0.3:
        st.warning(f"⚠ Medium Risk/suspicious transaction ...\nfraud probaility: {prob:.4f}")
    else:
        st.success(f"✅ Safe Transaction: {prob:.4f}")

# ---------------------------
# Option 2: Manual Input (simplified)
# ---------------------------
st.subheader("✍️ Enter Transaction Details")

input_data = {}

# Important features (from your feature importance)
important_cols = ['V4', 'V10', 'V14', 'V17']

for col in important_cols:
    input_data[col] = st.number_input(f"{col}", value=0.0)

# Convert to dataframe
input_df = pd.DataFrame([input_data])

# Fill missing columns with 0
input_df = input_df.reindex(columns=data.columns, fill_value=0)
if st.button("🔍 Predict Transaction"):

    prob = rf_model.predict_proba(input_df)[0][1]

    st.write("Fraud Probability:", prob)

    if prob > 0.7:
        st.error(f"🚨 Fraud Detected!high risk transation... Risk Score: {prob:.4f}")
    elif prob > 0.3:
        st.warning(f"⚠ Medium Risk/suspicious transaction ...\nfraud probaility: {prob:.4f}")
    else:
        st.success(f"✅ Safe Transaction: {prob:.4f}")