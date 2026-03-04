from flask import Flask, request, render_template_string
import os
import sqlite3
import subprocess
import pickle
import hashlib
import random

app = Flask(__name__)

# 1️⃣ Command Injection (os.system)
@app.route("/cmd")
def run_cmd():
    cmd = request.args.get("cmd")
    os.system(cmd)
    return "done"


# 2️⃣ SQL Injection
@app.route("/sql")
def get_user():
    email = request.args.get("email")
    query = "SELECT * FROM users WHERE email = '" + email + "'"
    conn = sqlite3.connect("db.sqlite3")
    conn.execute(query)
    return "done"


# 3️⃣ Path Traversal
@app.route("/read")
def read_file():
    filename = request.args.get("file")
    with open("./uploads/" + filename, "r") as f:
        return f.read()


# 4️⃣ Unsafe Deserialization
@app.route("/pickle")
def load_data():
    data = request.data
    obj = pickle.loads(data)
    return str(obj)


# 5️⃣ Hardcoded Secret
SECRET_KEY = "super-secret-api-key-123"


# 6️⃣ Insecure Random Token
@app.route("/token")
def generate_token():
    token = str(random.random())
    return token


# 7️⃣ Dangerous Eval
@app.route("/eval")
def run_code():
    code = request.args.get("code")
    eval(code)
    return "executed"


# 8️⃣ Subprocess Command Injection
@app.route("/subprocess")
def run():
    cmd = request.args.get("cmd")
    subprocess.call(cmd, shell=True)
    return "done"


# 9️⃣ Weak Hashing (MD5)
@app.route("/hash")
def hash_pass():
    password = request.args.get("password")
    return hashlib.md5(password.encode()).hexdigest()


# 🔟 Server Side Template Injection
@app.route("/template")
def render():
    tpl = request.args.get("tpl")
    return render_template_string(tpl)


if __name__ == "__main__":
    app.run(debug=True)