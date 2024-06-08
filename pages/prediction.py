# Notes
# do a "pip install streamlit" first 
# to run on terminal issue this command
# python -m streamlit run streamlit_test.py

import streamlit as st
import pandas as pd
import pickle

# Load the trained Naive Bayes classifier from the saved file
filename = 'pages/sentimentAnalyzerTest_Model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

st.title("Flood Cause Predictor :umbrella:")
st.subheader("Enter levels of different factors to determine the potential cause of the flood:")

# User inputs for different factors
urbanization_input = st.slider("Urbanization Level: ", 0, 500)
deforestation_input = st.slider("Deforestation Level: ", 0, 500)
agricultural_practices_input = st.slider("Intensity of Agricultural Practices: ", 0, 500)

# Function to make a prediction
def predict_flood_cause(urbanization, deforestation, agriculture):
    if urbanization == 0 and deforestation == 0 and agriculture == 0:
        return "No significant factors entered"
    else:
        prediction = loaded_model.predict([[urbanization, deforestation, agriculture]])
        return prediction[0]

# Display button and result
if st.button('Predict'):
    cause_of_flood = predict_flood_cause(urbanization_input, deforestation_input, agricultural_practices_input)
    st.text("The predicted cause of the flood is:")
    st.text_area(label="", value=cause_of_flood, height=100)
