from flask import Flask, request, jsonify
from deepface import DeepFace
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/verify_faces', methods=['POST'])
def verify_faces():
    if 'image1' not in request.files or 'image2' not in request.files:
        return jsonify({"error": "Please provide two images."}), 400

    file1 = request.files['image1']
    file2 = request.files['image2']

    file1_path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
    file2_path = os.path.join(app.config['UPLOAD_FOLDER'], file2.filename)
    file1.save(file1_path)
    file2.save(file2_path)

    result = DeepFace.verify(file1_path, file2_path)

    os.remove(file1_path)
    os.remove(file2_path)

    return jsonify({"verified": result['verified']}), 200

if __name__ == '__main__':
    app.run(debug=True)
