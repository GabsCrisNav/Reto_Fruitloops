import os
import sys
sys.path.append("../..")

from flask_cors import cross_origin
from PIL import Image
from flask import Blueprint, request, jsonify
from utils_model.predict_class import get_class
import json

predict = Blueprint('predict', __name__)

@predict.route('/predict', methods=['POST'])
@cross_origin()
def prediction_from_model():
    try:
        # Check if the POST request has the file part
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['file']
        
        # If user does not select file, browser also submit an empty part without filename
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        # Check if the file is allowed
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
        if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
            return jsonify({'error': 'Invalid file type'}), 400

        # Save the file to a temporary location
        upload_dir = 'uploads'
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        file_path = os.path.join(upload_dir, file.filename)
        file.save(file_path)
        
        # Process the uploaded image
        results = get_class(file_path, 0.1)

        # Delete the temporary file
        os.remove(file_path)

        return jsonify(results), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@predict.route('/test', methods=['POST'])
@cross_origin()
def test_model():
    try:
        # Path to a test image file
        image_path = "src/assets/test_m.jpeg"
        
        results = get_class(image_path, 0.6)
        
        return jsonify(results), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
