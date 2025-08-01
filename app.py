import pandas as pd
import pickle as pk
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st

# Load model and vectorizer
model = pk.load(open('model.pkl', 'rb'))
vectorizer = pk.load(open('vectorizer.pkl', 'rb'))  # Make sure this file exists in the same directory

# Streamlit UI
st.title("🎬 Movie Review Sentiment Analyzer")

# Text input
review = st.text_input('Enter Movie Review')

# Predict button
if st.button('Predict'):
    if review.strip() == "":
        st.warning("⚠️ Please enter a review.")
    else:
        # Vectorize the input review
        review_vector = vectorizer.transform([review])
        
        # Predict using the model
        result = model.predict(review_vector)
        
        # Display result
        if result[0] == 0:
            st.error('😞 Negative Review')
        else:
            st.success('😊 Positive Review')
