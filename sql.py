from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/user")
def user():
    email = request.args.get("email")
    query = "SELECT * FROM users WHERE email = '" + email + "'"
    conn = sqlite3.connect("db.sqlite3")
    conn.execute(query)
    return "ok"

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    conn = sqlite3.connect("db.sqlite3")
    conn.execute(query)
    return "ok"