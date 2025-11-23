from flask import Flask, request, jsonify
from pymongo import MongoClient
import numpy as np
import re
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the model from pickle file
with open('fake_review_detection.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the tokenizer from pickle file
with open('tokenizer.pickle', 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['TourXplore']
hotels_collection = db['hotels']

# Preprocessing function for reviews
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetical characters
    return text

# Home route to avoid 404 for root URL
@app.route('/')
def home():
    return "Welcome to the Fake Review Check API!"

# Route to check fake reviews in all hotels
@app.route('/api/review/check', methods=['GET'])
def check_fake_reviews():
    try:
        # Retrieve all hotels with reviews from MongoDB
        hotels = hotels_collection.find({'reviews': {'$exists': True, '$not': {'$size': 0}}})

        fake_reviews = []  # To store fake reviews

        for hotel in hotels:
            for review in hotel['reviews']:
                # Preprocess the review text
                cleaned_review = preprocess_text(review['comment'])

                # Use the tokenizer to process the review text
                review_seq = tokenizer.texts_to_sequences([cleaned_review])

                # Predict if the review is fake or real
                prediction = model.predict(review_seq)

                # Assuming '1' indicates a fake review and '0' real review
                predicted_class = np.argmax(prediction, axis=1)  # Get class with highest probability

                # If the review is fake (assuming '1' means fake)
                if predicted_class == 1:
                    fake_reviews.append({
                        'hotel_name': hotel['name'],
                        'reviewer': review['reviewer'],
                        'review': review['comment'],
                        'predicted': 'Fake'
                    })

        # If no fake reviews are found, return an appropriate message
        if not fake_reviews:
            return jsonify({"message": "No fake reviews found"}), 200
        
        # Return all the fake reviews detected
        return jsonify({"fake_reviews": fake_reviews}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message": "An error occurred while checking the reviews"}), 500

# Run the Flask app
if __name__ == '__main__':
    
    app.run(debug=False)

