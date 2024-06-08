

import streamlit as st
import pandas as pd
import pickle
from nltk.corpus import names

# Load the trained Naive Bayes classifier from the saved file
file = 'pages/sentimentAnalyzerTest_model.sav'
loaded_model = pickle.load(open(file, 'rb'))

st.title("Flood Cause Predictor :umbrella:")
st.subheader("Enter levels of different factors to determine the potential cause of the flood:")

# User inputs for different factors
rainfall_input = st.slider("Rainfall Level (mm): ", 0, 1000)
river_overflow_input = st.slider("River Overflow Level: ", 0, 100)
drainage_quality_input = st.slider("Drainage System Quality (1-10): ", 1, 10)
dam_condition_input = st.slider("Dam Condition (1-10): ", 1, 10)

# Function to make a prediction
def predict_flood_cause(rainfall, river_overflow, drainage_quality, dam_condition):
    if rainfall == 0 and river_overflow == 0 and drainage_quality == 1 and dam_condition == 1:
        return "No significant factors entered"
    else:
        features = {
            'rainfall': rainfall,
            'river_overflow': river_overflow,
            'drainage_quality': drainage_quality,
            'dam_condition': dam_condition
        }
        prediction = loaded_model.classify(features)
        return prediction

# Display button and result
if st.button('Predict'):
    cause_of_flood = predict_flood_cause(rainfall_input, river_overflow_input, drainage_quality_input, dam_condition_input)
    st.text("The predicted cause of the flood is:")
    st.text_area(label="", value=cause_of_flood, height=100)
