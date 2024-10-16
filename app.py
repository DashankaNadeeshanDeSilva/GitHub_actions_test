# This is the steamlit application for using an interface to batch and online prediction
import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("House Price Prediction")

# Real-time prediction
st.header("Real-Time Prediction")
square_feet = st.number_input("Enter square feet:", min_value=500, max_value=2000, step=50)
if st.button("Predict"):
    price = model.predict([[square_feet]])[0]
    st.write(f"The predicted price for {square_feet} square feet is ${price:.2f}")

# Batch prediction
st.header("Batch Prediction")
batch_input = st.text_area("Enter square feet values separated by commas (e.g., 800, 1000, 1200):")
if st.button("Batch Predict"):
    try:
        square_feet_list = [float(x) for x in batch_input.split(',')]
        predictions = model.predict(np.array(square_feet_list).reshape(-1, 1))
        st.write(f"Predicted prices: {predictions}")
    except:
        st.write("Please enter valid numeric values.")
