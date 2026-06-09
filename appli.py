import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("Loan Approval Prediction")

Gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

Married = st.selectbox(
    "Married",
    ["Yes", "No"]
)

Education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

Self_Employed = st.selectbox(
    "Self Employed",
    ["Yes", "No"]
)

Applicant_Income = st.number_input(
    "Applicant Income",
    min_value=0
)

Property_Area = st.selectbox(
    "Property Area",
    ["Urban", "Rural"]
)

if st.button("Predict"):

    payload = {
        "Gender": Gender,
        "Married": Married,
        "Education": Education,
        "Self_Employed": Self_Employed,
        "Applicant_Income": Applicant_Income,
        "Property_Area": Property_Area
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()

        st.success(
        f"Loan Status: {result['loan_status']['status']}"
        )

        st.write(
         f"Probability: {result['loan_status']['probability']}"
        )
    else:
        st.error(
            f"API Error: {response.text}"
        )