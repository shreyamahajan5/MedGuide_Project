import streamlit as st

st.title("💬 MedGuide Chatbot")

st.write("Ask your educational question below:")

user_input = st.text_input("You:", key="input")

# Simple hardcoded response logic (for demo)
def get_response(user_message):
    if "covid" in user_message.lower():
        return "COVID-19 is caused by SARS-CoV-2. Symptoms may include fever, cough, and fatigue."
    elif "pneumonia" in user_message.lower():
        return "Pneumonia is an infection that inflames the air sacs in one or both lungs."
    elif "hello" in user_message.lower():
        return "Hi there! I'm MedGuide, your educational assistant."
    else:
        return "I'm still learning! Please try asking something related to healthcare or biology."

if user_input:
    response = get_response(user_input)
    st.markdown(f"**MedGuide:** {response}")
