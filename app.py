
import streamlit as st
import pandas as pd
import joblib

# Load trained model and feature names
model = joblib.load("car_price_model.pkl")
feature_names = joblib.load("feature_names.pkl")

# Page configuration
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")

st.title("🚗 Car Price Predictor")
st.write("Enter the car details below to predict the estimated price.")

# ===========================
# User Inputs
# ===========================

brand = st.selectbox(
    "Brand",
    ["Tesla", "BMW", "Audi", "Ford", "Honda", "Mercedes", "Toyota"]
)

model_name = st.text_input("Model", "Model S")

) 

engine_size = st.number_input(
    "Engine Size (L)",
    min_value=0.5,
    max_value=8.0,
    value=2.0
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Electric", "Diesel", "Hybrid"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

mileage = st.number_input(
    "Mileage (km)",
    min_value=0,
    value=50000
)

condition = st.selectbox(
    "Condition",
    ["New", "Used", "Like New"]
)

# ===========================
# Prediction
# ===========================

if st.button("Predict Price"):

    input_df = pd.DataFrame({
        "Brand": [brand],
        "Model": [model_name], 
        "Engine Size": [engine_size],
        "Fuel Type": [fuel_type],
        "Transmission": [transmission],
        "Mileage": [mileage],
        "Condition": [condition]
    })

    # One-Hot Encoding
    input_df = pd.get_dummies(input_df)

    # Match training columns
    input_df = input_df.reindex(columns=feature_names, fill_value=0)

    # Prediction
    prediction = model.predict(input_df)[0]

    st.success(f"💰 Estimated Car Price: ${prediction:,.2f}")

st.markdown("---")
st.caption("Developed by Muhsan Tech | Machine Learning Project")
