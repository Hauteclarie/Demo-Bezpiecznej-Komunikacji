from flask import Flask, request, jsonify, render_template
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import sqlite3
import os

app = Flask(__name__)

# Secret key for AES encryption
SECRET_KEY = os.urandom(16)
IV = os.urandom(16)

# Database setup
def init_db():
    with sqlite3.connect('app.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, content TEXT)''')
        conn.commit()

# Encrypt a message using AES
def encrypt_message(message):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(IV), backend=backend)
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()

    encrypted_message = encryptor.update(padded_data) + encryptor.finalize()
    return encrypted_message

# Decrypt a message using AES
def decrypt_message(encrypted_message):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(IV), backend=backend)
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(encrypted_message) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return unpadded_data.decode()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form['message']
    encrypted_message = encrypt_message(message)
    return jsonify({"encrypted": encrypted_message.hex()})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_message = bytes.fromhex(request.form['encrypted'])
    decrypted_message = decrypt_message(encrypted_message)
    return jsonify({"decrypted": decrypted_message})

@app.route('/sql_injection_demo', methods=['POST'])
def sql_injection_demo():
    user_input = request.form['input']
    with sqlite3.connect('app.db') as conn:
        cursor = conn.cursor()

        # Vulnerable query (SQL Injection demonstration)
        try:
            cursor.execute(f"SELECT * FROM messages WHERE content = '{user_input}'")
            result = cursor.fetchall()
            return jsonify({"result": result})
        except Exception as e:
            return jsonify({"error": str(e)})

@app.route('/secure_query', methods=['POST'])
def secure_query():
    user_input = request.form['input']
    with sqlite3.connect('app.db') as conn:
        cursor = conn.cursor()

        # Secure query using parameterized input
        cursor.execute("SELECT * FROM messages WHERE content = ?", (user_input,))
        result = cursor.fetchall()
        return jsonify({"result": result})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
