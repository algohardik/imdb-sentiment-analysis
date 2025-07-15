import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.datasets import imdb
import re

maxlen = 500
max_features = 10000

# Load model
model = tf.keras.models.load_model("model/sentiment_model.keras")

# Load word index
word_index = imdb.get_word_index()

def preprocess_review(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

def tokenize_review(text):
    tokens = text.split()
    mapped = [(word, word_index.get(word, 2)) for word in tokens]
    return [index + 3 if index < max_features else 2 for _, index in mapped], mapped

def predict_sentiment(text):
    cleaned = preprocess_review(text)
    token_ids, token_mapping = tokenize_review(cleaned)
    padded = pad_sequences([token_ids], maxlen=maxlen)
    prob = float(model.predict(padded, verbose=0)[0][0])
    label = "Positive" if prob > 0.5 else "Negative"
    return cleaned, token_mapping, padded.shape, prob, label

# Streamlit UI
st.title("🎬 IMDB Movie Review Sentiment Analyzer")
user_input = st.text_area("Enter your movie review here:")

if st.button("Analyze"):
    if user_input.strip():
        cleaned, token_mapping, pad_shape, prob, label = predict_sentiment(user_input)
        st.markdown("### 🧼 Cleaned Review:")
        st.write(cleaned)
        st.markdown("### 🔎 Token Mapping:")
        st.text("\n".join([f"{w:>15} → {i}" for w, i in token_mapping]))
        st.markdown("### 📦 Padded Review Shape:")
        st.code(pad_shape)
        st.markdown("### 📊 Predicted Sentiment:")
        st.success(f"{label} (Probability: {prob:.4f})")