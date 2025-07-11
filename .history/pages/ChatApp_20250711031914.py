import streamlit as st
import json
import numpy as np
import random
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Title
st.title("💬 MedGuide - AI Educational Chatbot")

st.write("Ask me anything about medical terms, diseases, symptoms, or AI!")

# Load resources
lemmatizer = WordNetLemmatizer()

with open("intents.json", encoding='utf-8') as file:
    intents = json.load(file)

model = pickle.load(open("chatbot_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Text preprocessing
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def predict_class(sentence):
    sentence_words = clean_up_sentence(sentence)
    sentence_joined = " ".join(sentence_words)
    X = vectorizer.transform([sentence_joined])
    predictions = model.predict_proba(X)[0]
    threshold = 0.3
    results = [{"intent": i, "prob": prob} for i, prob in enumerate(predictions) if prob > threshold]
    results.sort(key=lambda x: x["prob"], reverse=True)
    return results

def get_response(ints, intents_json):
    if not ints:
        return "I'm not sure I understand. Could you try asking in a different way?"
    tag = intents_json['intents'][ints[0]['intent']]['tag']
    for i in intents_json['intents']:
        if i['tag'] == tag:
            return random.choice(i['responses'])

# Chat input
user_input = st.text_input("You:", "")

if user_input:
    intents_list = predict_class(user_input)
    response = get_response(intents_list, intents)
    st.markdown(f"**MedGuide:** {response}")
