from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import os
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Enable CORS for React frontend on port 5173
CORS(app, origins=["http://localhost:5173"])

# Flask configuration for uploaded files
app.config['UPLOADED_RESUMES_DEST'] = 'uploads'  # Directory to store resumes
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create directory for uploads if it doesn't exist
if not os.path.exists(app.config['UPLOADED_RESUMES_DEST']):
    os.makedirs(app.config['UPLOADED_RESUMES_DEST'])

# Load pre-trained model and vectorizer
model = joblib.load('resume_classifier_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Path to store resume information as a JSON file
RESUMES_JSON_PATH = 'resumes.json'

# Function to load resume data from the JSON file
def load_resumes():
    if os.path.exists(RESUMES_JSON_PATH):
        with open(RESUMES_JSON_PATH, 'r') as f:
            return json.load(f)
    else:
        return []

# Function to save resume data to the JSON file
def save_resumes(resumes):
    with open(RESUMES_JSON_PATH, 'w') as f:
        json.dump(resumes, f, indent=4)

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    if file:
        filepath = os.path.join(app.config['UPLOADED_RESUMES_DEST'], secure_filename(file.filename))
        file.save(filepath)  # Save file to the server
        
        # Read and process the resume text for prediction
        with open(filepath, 'r') as f:
            resume_text = f.read()

        # Vectorize the resume text
        features = vectorizer.transform([resume_text])

        # Get predicted class probabilities
        probabilities = model.predict_proba(features)[0]
        predicted_class_index = probabilities.argmax()  # Find the class with the highest probability
        predicted_category = model.classes_[predicted_class_index]  # Map index to category
        confidence_score = probabilities[predicted_class_index]  # Confidence score (probability)

        # Load existing resumes
        resumes = load_resumes()

        # Create a new resume entry
        new_resume = {
            'filename': file.filename,
            'category': predicted_category,
            'confidence': confidence_score,
            'filepath': f'/uploads/{file.filename}'  # Update to correct URL for file access
        }

        # Add the new resume to the list and save it
        resumes.append(new_resume)
        save_resumes(resumes)

        return jsonify({
            "category": predicted_category,
            "confidence_score": confidence_score,
            "file": f'/uploads/{file.filename}'  # Send URL for frontend to access
        })
    
    return jsonify({"error": "No file provided"}), 400

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
