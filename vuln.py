import os
import subprocess
import sqlite3
import requests
import xml.etree.ElementTree as ET
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# Vulnerable AWS Key
KEY = "AKIA2F5UPF3FJR2J5RNE"
SECRET = "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"

GITHUB_TOKEN = "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"

# Firebase API Key
FIREBASE_API_KEY_1 = "AIzaSyD3F1J-affc104XOz45LmNoPQRSTUvwXYZ"
FIREBASE_API_KEY_2 = 'AIzaSyA7Z5F1-bcdE234XZ56LmOpQRSUVwyX789'
FIREBASE_API_KEY_3 = 'AIzaSyB8G2G1-efgH345YZ67LmNpQRSTVwxY012'
FIREBASE_API_KEY_4 = 'AIzaSyC9H3H1-hijI456XY78LnOqRSTUWxyZ345'
FIREBASE_API_KEY_5 = 'AIzaSyD0J4I1-klmJ567YX89LmPqRSTUVxzA678'
FIREBASE_API_KEY_6 = 'AIzaSyE1K5J1-nopK678ZX90LnQrSTUVWxy'



# Private Key hardcoded
PRIVATE_KEY = """
-----BEGIN RSA PRIVATE KEY-----
MIIBOgIBAAJBAKj34GkxFhD90vcNLYLInFEX6Ppy1tPf9Cnzj4p4WGeKLs1Pt8Qu
KUpRKfFLfRYC9AIKjbJTWit+CqvjWYzvQwECAwEAAQJAIJLixBy2qpFoS4DSmoEm
o3qGy0t6z09AIJtH+5OeRV1be+N4cDYJKffGzDa88vQENZiRm0GRq6a+HPGQMd2k
TQIhAKMSvzIBnni7ot/OSie2TmJLY4SwTQAevXysE2RbFDYdAiEBCUEaRQnMnbp7
9mxDXDf6AU0cN/RPBjb9qSHDcWZHGzUCIG2Es59z8ugGrDY+pxLQnwfotadxd+Uy
v/Ow5T0q5gIJAiEAyS4RaI9YG8EWx/2w0T67ZUVAw8eOMB6BIUg0Xcu+3okCIBOs
/5OiPgoTdSy7bcF9IGpSE8ZgGKzgYQVZeN97YE00
-----END RSA PRIVATE KEY-----
"""

# Username/Password hardcoded
DB_USERNAME = "admin"
DB_PASSWORD = "P@ssword123"

# Database URL with credentials
DATABASE_URL = "mysql://user:password@database.example.com:3306/mydb"

# API Key hardcoded
API_KEY_1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
API_KEY_2 = '1a2b3c4d-5678-9101-1121-314151617181'
API_KEY_3 = 'abcd1234-efgh-5678-ijkl-91011mnopqr'
API_KEY_4 = '12345678-abcd-1234-efgh-567890ijklmn'
API_KEY_5 = 'qwertyui-1234-5678-asdf-ghjklzxcvbnm'
API_KEY_6 = 'api_5678ABCD-EFGH-91011-IJKL-121314MNOPQR'
API_KEY_7 = '9f8e7d6c-5b4a-3210-1q2w3e4r5t6y7u8i'
API_KEY_8 = 'API-1234567890ABCDEFGHIJKLMNOPQRST'
API_KEY_9 = 'key_abcdef1234567890ghijklmnopqrst'
API_KEY_10 = 'ZXCVBNMLKJHGFDSAQWERTYUIOP0987654321'
API_KEY_11 = 'apikey_11223344556677889900AABBCCDD'




# Path Traversal Vulnerability
@app.route("/read-file", methods=["GET"])
def read_file():
    filename = request.args.get("file")
    filepath = os.path.join("/var/www/files", filename)  
    with open(filepath, "r") as file:
        return file.read()


# Insecure File Upload
@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    file.save(f"/uploads/{file.filename}")  
    return "File uploaded successfully!"


# XSS Vulnerability
@app.route("/xss", methods=["GET"])
def xss():
    user_input = request.args.get("input", "")
    template = f"<h1>User Input: {user_input}</h1>"
    return render_template_string(template) 


# SQL Injection Vulnerability
@app.route("/sql-injection", methods=["GET"])
def sql_injection():
    user_input = request.args.get("username", "")
    conn = sqlite3.connect("example.db")
    query = f"SELECT * FROM users WHERE username = '{user_input}'"  
    cursor = conn.execute(query)
    result = cursor.fetchall()
    return str(result)


# XML External Entity (XXE) Injection
@app.route("/xxe", methods=["POST"])
def xxe():
    xml_data = request.data.decode("utf-8")
    tree = ET.fromstring(xml_data)  
    return tree.tag


# Server-Side Request Forgery (SSRF)
@app.route("/ssrf", methods=["GET"])
def ssrf():
    url = request.args.get("url")
    response = requests.get(url) 
    return response.text


# Open Redirect Vulnerability
@app.route("/redirect", methods=["GET"])
def open_redirect():
    url = request.args.get("url")
    return redirect(url)  


# Command Injection
@app.route("/command", methods=["POST"])
def command_injection():
    user_command = request.form.get("cmd")
    result = subprocess.check_output(user_command, shell=True)  
    return result


# Run the application
if __name__ == "__main__":
    app.run(debug=True)
