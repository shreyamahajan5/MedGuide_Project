# 🩺 MedGuide

**AI-Powered Chest X-ray Diagnostic System with Smart Medical Chat Support**


## 🌐 Live App

🔗 https://huggingface.co/spaces/shreyamahajan5/MedGuide

---

## 📌 Project Summary

**MedGuide** is an intelligent healthcare application built to assist in **chest X-ray diagnosis** using deep learning and to provide basic medical information through a chatbot assistant. Designed for both **students** and **healthcare professionals**, the tool streamlines early detection and learning.

---

## 🫁 Core Feature: Chest X-ray Disease Detection

### ✅ What It Does:
Upload a chest X-ray image, and the system uses a trained convolutional neural network to detect:

- **COVID-19**
- **Pneumonia**
- **Tuberculosis**
- **Normal (Healthy)**

### ✅ Why It Matters:
- Speeds up preliminary analysis in remote or understaffed settings
- Assists medical students in learning how X-ray diagnostics work
- Enables early triage before formal testing

### 🧠 How It Works:
- Pre-trained deep learning model (`.h5`) built using TensorFlow/Keras
- Image preprocessing using OpenCV & PIL
- Streamlit-based interactive UI for image upload and result display

---

## 💬 Educational Chatbot (Secondary Feature)

While the X-ray model handles diagnostics, the **built-in chatbot** allows users to:
- Ask health-related questions (e.g., “What is pneumonia?”)
- Learn about diseases and their symptoms
- Understand diagnostic methods in a friendly, conversational manner

Built using:
- `scikit-learn` + `TF-IDF` + `LogisticRegression`
- `intents.json` for pattern–response mapping

---

## 🖼️ Interface Preview

MedGuide/
├── MedGuide.py # Main app: X-ray predictor
├── pages/
│ └── ChatApp.py # Medical chatbot
├── chatbot_model.pkl # Trained ML model for chatbot
├── vectorizer.pkl # TF-IDF vectorizer
├── intents.json # Chatbot Q&A dataset
├── README.md # This file


---

## 🚀 How to Run

1. Clone the Repo

```bash
git clone https://github.com/your-username/MedGuide.git
cd MedGuide

]2. Install Requirements

```bash
pip install streamlit tensorflow opencv-python scikit-learn pillow

3. Launch the App
```bash
streamlit run MedGuide.py

📚 Use Cases

🧪 Upload an X-ray for AI-based diagnosis
🧠 Ask basic health-related questions
🧑‍🎓 Use it as an educational tool to learn medical imaging
🏥 Prototype assistant for clinics and telehealth platforms

🛠 Technologies Used

Python
Streamlit
TensorFlow / Keras
OpenCV
scikit-learn
JSON (for NLP intents)

## 👩‍💻 Author

Shreya Mahajan
LinkedIn | GitHub

