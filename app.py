from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["mydatabase"]   # change to your db name
scores_collection = db["scores"]

# GET: fetch top 10 scores
@app.route('/api/scores', methods=['GET'])
def get_scores():
    try:
        top_scores = list(scores_collection.find().sort("score", -1).limit(10))
        for score in top_scores:
            score["_id"] = str(score["_id"])  # convert ObjectId to string
        return jsonify(top_scores), 200
    except Exception as e:
        return jsonify({"message": "Error fetching scores", "error": str(e)}), 500

# POST: add new score
@app.route('/api/scores', methods=['POST'])
def add_score():
    try:
        data = request.get_json()
        name = data.get("name")
        score = data.get("score")

        if not name or score is None:
            return jsonify({"message": "Name and score are required."}), 400

        new_score = {
            "name": name.strip()[:15],  # trim + maxLength 15
            "score": int(score),
            "timestamp": datetime.utcnow()
        }

        result = scores_collection.insert_one(new_score)
        new_score["_id"] = str(result.inserted_id)
        return jsonify(new_score), 201
    except Exception as e:
        return jsonify({"message": "Error saving score", "error": str(e)}), 500

if __name__ == '__main__':
    PORT = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)
