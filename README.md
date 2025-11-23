Smart Tourism with VR & Fake Review Detection

A modern AI-powered travel assistant that generates personalized itineraries, detects fake reviews using LSTM, enhances destination images using Real-ESRGAN, and offers immersive VR previews.
Built using AI + NLP + Deep Learning + VR + GANs + Real-Time APIs.

✨ Project Highlights
• AI-Based Personalized Travel Planning

Generates day-wise itineraries

Uses real-time hotel & flight pricing

Budget optimization

User-preference filtering

Dynamic recalculation

• Fake Review Detection (LSTM Model)

Detects:

Genuine Reviews

Human-Written Fake Reviews

GPT-Generated Fake Reviews

Includes:

NLP preprocessing

LSTM deep learning classifier

Accuracy: 93.5%

• Real-ESRGAN Image Upscaling

Enhances low-resolution destination images

GAN-based super-resolution

Improves clarity for VR previews

• VR Destination Preview

Unity-based 360° virtual tours

Explore places before visiting

Immersive, interactive experience

🧠 System Architecture
1️⃣ Itinerary Generator (AI Module)

Processes user budget, dates & preferences

Fetches real-time travel data

Generates ideal route & schedule

2️⃣ Fake Review Detection Module

Text cleaning + tokenization

LSTM classification pipeline

Flags deceptive reviews

3️⃣ ESRGAN Image Upscaling

Input: low-resolution images

Output: high-quality VR-ready images

4️⃣ VR Experience Engine

Unity 3D environment

Panoramic view rendering

🗄 Databases

tourism.db – itineraries, VR assets, image paths

reviews.db – reviews + authenticity labels

💻 Tech Stack

Backend: Python, Flask
AI/ML: TensorFlow, Keras, LSTM, Scikit-learn
NLP: Tokenizer, stop-word removal, text normalization
VR: Unity 3D / Three.js
Image Processing: Real-ESRGAN (PyTorch)
Frontend: React Native / Flutter
Database: MongoDB

⚙️ How to Run the Project
1. Clone the Repository
git clone https://github.com/Dhanusree28/smart-tourism-review-detection.git
cd smart-tourism-review-detection

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Linux/Mac

3. Install Dependencies
pip install -r requirements.txt

4. Run the Flask App
python app.py

5. Run ESRGAN Upscaler
python upscale.py --input images/ --output results/

6. Open VR Module

Open the folder:

/vr/UnityProject/


in Unity Hub.
