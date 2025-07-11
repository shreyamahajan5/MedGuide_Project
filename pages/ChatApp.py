import streamlit as st
import json
import pickle
import numpy as np
import random

# Load data files
with open("intents.json", encoding="utf-8") as file:
    intents = json.load(file)

model = pickle.load(open("chatbot_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Streamlit app UI
st.title("💬 MedGuide - AI Educational Chatbot")
st.write("Ask me anything about medical conditions like COVID-19, pneumonia, or TB.")

# Helper to match intent
def predict_intent(user_input):
    X = vectorizer.transform([user_input.lower()])
    probabilities = model.predict_proba(X)[0]
    threshold = 0.3
    filtered = [{"intent": idx, "prob": prob} for idx, prob in enumerate(probabilities) if prob > threshold]
    filtered.sort(key=lambda x: x["prob"], reverse=True)
    return filtered

def get_response(predictions):
    if not predictions:
        return "Sorry, I couldn't understand that. Can you rephrase?"
    tag_idx = predictions[0]['intent']
    tag = list({i['tag'] for i in intents['intents']})[tag_idx]
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "Hmm... I'm not sure how to help with that yet."

# Chat logic
user_input = st.text_input("You:", "")

if user_input:
    predictions = predict_intent(user_input)
    bot_reply = get_response(predictions)
    st.markdown(f"**MedGuide:** {bot_reply}")
