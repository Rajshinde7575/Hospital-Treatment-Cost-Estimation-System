import streamlit as st
import pandas as pd
import pickle as pkl

# Title
st.title("HEALTH EXPENSE COST PREDICTION")

# Inputs
age = st.number_input(
    "Select Age",
    min_value=18,
    max_value=100,
    value=25
)

gender = st.selectbox("Select Gender", ["male", "female"])

bmi = st.number_input(
    "Enter BMI",
    min_value=10,
    max_value=60,
    value=25
)

children = st.number_input(
    "Enter Number of Children",
    min_value=0,
    max_value=5,
    value=0
)

smoker = st.selectbox("Select Smoker", ["YES", "NO"])

region = st.selectbox(
    "Select Region",
    ["northeast", "southeast"]
)

# Load model
model = pkl.load(open("insurance_model.pkl", "rb"))

# Prediction
if st.button("Predict"):

    gender_value = 1 if gender == "male" else 0
    smoker_value = 1 if smoker == "YES" else 0

    region_map = {
        "northeast": 0,
        "southeast": 1
    }

    region_value = region_map[region]

    input_data = pd.DataFrame(
        [[age, gender_value, bmi, children, smoker_value, region_value]],
        columns=["age", "gender", "bmi", "children", "smoker", "region"]
    )

    prediction = model.predict(input_data)

    st.success(f"Estimated Expense Cost: ₹{prediction[0]:,.2f}")