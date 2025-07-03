import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load("diabetic_retinopathy_model (2).pkl")

# Streamlit UI
st.title("Diabetic Retinopathy Prediction")

# User input fields with appropriate min-max values
age = st.number_input("Age", min_value=35.16, max_value=103.28, step=0.1)
systolic_bp = st.number_input("Systolic Blood Pressure", min_value=69.67, max_value=151.70, step=0.1)
diastolic_bp = st.number_input("Diastolic Blood Pressure", min_value=62.81, max_value=133.46, step=0.1)
cholesterol = st.number_input("Cholesterol", min_value=69.97, max_value=148.23, step=0.1)

# Predict button
if st.button("Predict"):
    # Convert input to numpy array
    user_input = np.array([[age, systolic_bp, diastolic_bp, cholesterol]])
    
    # Make prediction
    prediction = model.predict(user_input)
    
    # Display result
    if prediction[0] == 1:
        st.error(" Diabetic retinopathy detected.")
    else:
        st.success("NO Diabetic Retinopathy.")
