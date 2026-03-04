from flask import Flask, request

app = Flask(__name__)

@app.route("/read")
def read_file():
    filename = request.args.get("file")
    with open("./uploads/" + filename) as f:
        return f.read()

@app.route("/write")
def write_file():
    name = request.args.get("name")
    open("/tmp/" + name, "w").write("data")
    return "ok"