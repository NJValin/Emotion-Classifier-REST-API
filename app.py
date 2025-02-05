from flask import Flask, jsonify, request
from transformers import pipeline
#import torch


classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)
app = Flask(__name__)


@app.route("/")
def index():
    return "Model Running"

@app.route("/classify", methods=["POST"])
def classify():
    try:
        data = request.get_data()

        classification = classifier(str(data))

        return jsonify(classification)

    except Exception as e:
        return jsonify({"error":str(e)}), 500
