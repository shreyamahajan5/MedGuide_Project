import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import os

# Constants
MODEL_PATH = 'ChestXray.h5'
TARGET_SIZE = (150, 150)
CLASS_LABELS = ["COVID19", "NORMAL", "PNEUMONIA", "TUBERCULOSIS"]

# Initialize session state for storing predictions
if 'predictions' not in st.session_state:
    st.session_state.predictions = None
if 'uploaded_image' not in st.session_state:
    st.session_state.uploaded_image = None

def load_model():
    try:
        if not os.path.exists(MODEL_PATH):
            st.error(f"Model file not found at {MODEL_PATH}. Please ensure the model file is in the correct location.")
            return None
        return tf.keras.models.load_model(MODEL_PATH)
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

# Load the model
loaded_model = load_model()

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://plus.unsplash.com/premium_photo-1661634247664-ac7d0f00cf0c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1771&q=80");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

def homepage():
    st.title("Welcome to MedGuide")
    st.write("<span style='font-size:30px;colour:white'><b>X-ray analysis for Tuberculosis, COVID-19, and Pneumonia</b></span>", unsafe_allow_html=True)
    add_bg_from_url()

def user_info():
    st.title("User Information")
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0, max_value=120)
    gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
    
    if name and age:
        st.session_state.user_info = {
            "name": name,
            "age": age,
            "gender": gender
        }
        st.success("User information saved successfully!")

def preprocess_image(img):
    try:
        if isinstance(img, str):
            img = Image.open(img)
        elif isinstance(img, np.ndarray):
            img = Image.fromarray(img)
        
        img = img.convert('RGB')
        img = img.resize(TARGET_SIZE)
        img_array = image.img_to_array(img)
        img_array = img_array / 255.0  # Normalize pixel values
        img_array = np.expand_dims(img_array, axis=0)
        return img_array
    except Exception as e:
        st.error(f"Error preprocessing image: {str(e)}")
        return None

def xray_upload():
    st.title("X-ray Upload and Prognosis")
    
    if loaded_model is None:
        st.error("Model not loaded. Please check the model file.")
        return

    uploaded_file = st.file_uploader("Upload your X-ray image (JPEG or PNG):", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        try:
            # Save the uploaded file temporarily
            img = Image.open(uploaded_file)
            st.session_state.uploaded_image = img
            
            # Display the uploaded image
            st.image(img, caption="Uploaded Image", use_column_width=True)
            
            # Preprocess and predict
            processed_img = preprocess_image(img)
            if processed_img is not None:
                predictions = loaded_model.predict(processed_img)
                st.session_state.predictions = predictions[0]
                
                # Display predictions
                st.subheader("Prediction Results:")
                for i, label in enumerate(CLASS_LABELS):
                    confidence = predictions[0][i] * 100
                    st.write(f"{label}: {confidence:.2f}%")
                    st.progress(confidence / 100.0)
                
                # Get the predicted class
                predicted_class = CLASS_LABELS[np.argmax(predictions[0])]
                st.success(f"Predicted Condition: {predicted_class}")
                
                # Provide health tips
                provide_tips(predicted_class)
                
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")

def provide_tips(predicted_class_label):
    st.subheader("Health Tips")
    tips = {
        "COVID19": [
            "Please follow your healthcare provider's instructions and quarantine yourself.",
            "Maintain proper hygiene, wear a mask, and practice social distancing.",
            "Monitor your symptoms and seek immediate medical attention if they worsen."
        ],
        "NORMAL": [
            "Your X-ray shows no signs of any lung disease.",
            "Continue to maintain a healthy lifestyle with a balanced diet and regular exercise.",
            "Schedule regular check-ups with your healthcare provider."
        ],
        "PNEUMONIA": [
            "Please consult your doctor immediately for further evaluation and treatment.",
            "Rest, stay hydrated, and follow your doctor's recommendations.",
            "Take prescribed medications as directed and complete the full course of antibiotics."
        ],
        "TUBERCULOSIS": [
            "Please consult your doctor immediately for further evaluation and treatment.",
            "Follow your doctor's treatment plan and take medications as prescribed.",
            "Complete the full course of treatment to prevent drug resistance."
        ]
    }
    
    for tip in tips.get(predicted_class_label, []):
        st.write(f"• {tip}")

def reviews_feedback():
    st.title("Reviews and Feedback")
    feedback = st.text_area("Give us your feedback:")
    rating = st.slider("Rate your experience (1-10):", 1, 10)
    
    if st.button("Submit Feedback"):
        if feedback:
            st.success("Thank you for your feedback!")
            st.write(f"Rating: {rating}/10")
            st.write(f"Feedback: {feedback}")
        else:
            st.warning("Please provide some feedback before submitting.")

# Main app
def main():
    st.set_page_config(page_title="MedGuide", page_icon="🏥", layout="wide")
    
    # Sidebar Navigation
    page = st.sidebar.selectbox("Select a page:", ["Home", "User Info", "X-ray Upload", "Reviews & Feedback"])
    
    # Display Pages Based on Selection
    if page == "Home":
        homepage()
    elif page == "User Info":
        user_info()
    elif page == "X-ray Upload":
        xray_upload()
    elif page == "Reviews & Feedback":
        reviews_feedback()

if __name__ == "__main__":
    main()
