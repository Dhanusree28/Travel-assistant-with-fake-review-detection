Smart Tourism with VR & Fake Review Detection

An AI-powered travel assistant that generates personalized itineraries, detects fake reviews using LSTM, enhances destination images using Real-ESRGAN, and provides immersive Virtual Reality destination previews.
The system integrates AI + NLP + Deep Learning + VR + GANs to modernize and secure the travel planning experience.

🚀 Project Highlights
🔹 AI-Based Personalized Travel Planning

Generates day-wise itineraries based on:

Budget

Travel dates

User preferences

Real-time flight & hotel prices

Dynamic budget recalibration

Uses live travel APIs

🔹 Fake Review Detection (LSTM)

Detects:

Genuine reviews

Human-written fake reviews

GPT-generated fake reviews (optional extension)

Model Features:

LSTM classifier

NLP preprocessing (tokenization, stop-words, normalization)

Accuracy: 93.5%

Precision/Recall balanced

🔹 Image Upscaling using Real-ESRGAN

Upscales low-resolution destination images

Improves quality for VR previews

Removes blur, restores texture

🔹 VR Destination Preview

Unity-powered 360° virtual exploration

View landmarks before visiting

Enhances user decision-making

🧠 System Architecture
1) AI Itinerary Generator

Collects user inputs

Fetches real-time data

Builds optimized travel schedules

Recalculates budget dynamically

2) Fake Review Detection Module

LSTM classifier

Preprocessing pipeline

Flags suspicious reviews

Ensures trustworthy content

3) Image Upscaler (Real-ESRGAN)

GAN-based super-resolution

Enhances images for web & VR

4) VR Experience Engine

Renders 3D environments

Provides immersive virtual tours

Databases

tourism.db – itineraries, images, VR resources

reviews.db – user reviews + authenticity tags

🗂 Tech Stack
Component	Technology
Backend	Python, Flask
AI/ML	LSTM, TensorFlow, Keras, Scikit-learn
NLP	Tokenizer, Padding, Text cleaning
VR	Unity3D / Three.js
Image Processing	Real-ESRGAN (PyTorch)
Database	MongoDB
Frontend	React Native / Flutter
⚙️ How to Run the Project
1. Clone the Repository
git clone https://github.com/Dhanusree28/smart-tourism-review-detection.git
cd smart-tourism-review-detection

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac

3. Install Dependencies
pip install -r requirements.txt

4. Run the Flask API
python app.py

5. Run ESRGAN Upscaler
python upscale.py --input images/ --output results/

6. Open VR Module (Unity Project)

Open the /vr/UnityProject/ folder in Unity Hub.
