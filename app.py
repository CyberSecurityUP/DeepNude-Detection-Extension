from flask import Flask, request, jsonify
from flask_cors import CORS  # Importando o CORS
from nudenet import NudeClassifier
import requests
import os
import random
import string

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Permite todas as origens

class NudeDetector:
    def __init__(self):
        self.classifier = NudeClassifier()

    def generate_random_name(self, length=5):
        return ''.join(random.choices(string.ascii_lowercase, k=length))

    def download_image_from_url(self, url):
        random_name = self.generate_random_name()
        save_path = f"{random_name}.jpg"
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as out_file:
                out_file.write(response.content)
            return save_path
        else:
            return None

    def detect(self, img_path, min_prob=0.84):
        result = self.classifier.classify(img_path)
        detections = []
        for image, output in result.items():
            if output['unsafe'] >= min_prob:
                detections.append({
                    'image': image,
                    'unsafe_score': output['unsafe'],
                    'improper': True
                })
            else:
                detections.append({
                    'image': image,
                    'unsafe_score': output['unsafe'],
                    'improper': False
                })
        return detections

@app.route('/detect_nude', methods=['POST'])
def detect_nude():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    detector = NudeDetector()
    img_path = detector.download_image_from_url(url)
    if not img_path:
        return jsonify({"error": "Failed to download image"}), 500

    results = detector.detect(img_path)
    os.remove(img_path)  # Remove the downloaded image

    return jsonify({"detections": results})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
