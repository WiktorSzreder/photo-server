from flask import Flask, request, send_from_directory, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return jsonify({"message": "File uploaded successfully"}), 200

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/')
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    links = [f'<a href="/uploads/{f}">{f}</a>' for f in files]
    return '<br>'.join(links)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
