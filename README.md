# FUTURE_CS_03
# 🔐 Secure File Sharing System using Flask and AES Encryption

This project is a secure file sharing web application built with Python Flask. It enables users to **upload and download files with AES encryption**, ensuring data confidentiality and security — a simulation of real-world secure data sharing in domains like healthcare, law, and enterprise.

---

## 🚀 Features

- 🔐 AES encryption (AES-128, CBC mode) for file security
- ⬆️ Upload files with automatic encryption
- ⬇️ Download files with secure decryption
- 🌐 Web interface with Flask and HTML
- 🗂️ Encrypted files stored separately (`uploads/`)
- 📁 Decrypted files served temporarily (`temp/`)
- 💼 Basic encryption key management

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Encryption:** PyCryptodome (AES)
- **Frontend:** HTML5, CSS3
- **Version Control:** Git & GitHub

---

## 🏗️ Project Structure
FUTURE_CS_03/
├── app.py # Flask application logic
├── encryption.py # AES encryption/decryption functions
├── templates/
│ └── index.html # Upload/Download UI
├── uploads/ # Encrypted files
├── temp/ # Temporary decrypted files
├── requirements.txt # Python dependencies
└── README.md # This file

## 🧪 Testing
Upload any file (e.g. .txt, .jpg, .pdf)

Check uploads/ for encrypted .enc file

Download and verify the file integrity

## 🔐 Encryption Details
Algorithm: AES (Advanced Encryption Standard)

Mode: CBC (Cipher Block Chaining)

Key: 16-byte static key (b'ThisIsASecretKey') for demo

Security: IV is prepended for decryption context

⚠️ Note: In production, store keys securely using environment variables or secret managers.

## 📌 To-Do / Future Enhancements
 Use secure key storage (e.g., .env)

 Add user authentication

 Display uploaded file list in frontend

 Automatically clear decrypted temp files

 Add logging and size limits

## 📄 License
This project is built for educational purposes under the internship program at Future Interns. No commercial use without permission.

