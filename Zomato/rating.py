import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model.pkl')

st.title("Zomato Restaurant Rating Predictor")

st.write("""
Predict the rating of a restaurant based on key features.
""")

# Input features
online_order = st.selectbox("Online Order Available?", ["Yes", "No"])
book_table = st.selectbox("Book Table Available?", ["Yes", "No"])
votes = st.number_input("Number of Votes", min_value=0, step=1)
approx_cost = st.number_input("Approx Cost for Two People", min_value=0)

# Convert inputs to model-ready format
input_data = pd.DataFrame({
    'online_order': [1 if online_order == "Yes" else 0],
    'book_table': [1 if book_table == "Yes" else 0],
    'votes': [votes],
    'approx_cost(for two people)': [approx_cost]
})

# Predict button
if st.button("Predict Rating"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Restaurant Rating: {round(prediction[0], 2)} / 5")
