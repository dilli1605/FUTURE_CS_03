from flask import Flask, render_template, request, send_file
import os
from encryption import encrypt_file, decrypt_file

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
TEMP_FOLDER = 'temp'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(TEMP_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    data = file.read()
    encrypted_data = encrypt_file(data)

    encrypted_path = os.path.join(UPLOAD_FOLDER, file.filename + '.enc')
    with open(encrypted_path, 'wb') as f:
        f.write(encrypted_data)

    return 'File uploaded and encrypted successfully!'

@app.route('/download/<filename>')
def download_file(filename):
    encrypted_path = os.path.join(UPLOAD_FOLDER, filename + '.enc')

    with open(encrypted_path, 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = decrypt_file(encrypted_data)
    decrypted_path = os.path.join(TEMP_FOLDER, filename)

    with open(decrypted_path, 'wb') as f:
        f.write(decrypted_data)

    return send_file(decrypted_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
