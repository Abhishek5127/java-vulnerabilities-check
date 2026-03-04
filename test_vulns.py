from flask import Flask, request
import zipfile
import tempfile
import yaml

app = Flask(__name__)

# 1️⃣ Format String Injection
@app.route("/format")
def format_injection():
    msg = request.args.get("msg")
    print(msg % {"user": "admin"})
    return "done"


# 2️⃣ Zip Slip (Archive Path Traversal)
@app.route("/zip")
def zip_slip():
    file = request.files["file"]
    z = zipfile.ZipFile(file)
    z.extractall("./uploads")
    return "unzipped"


# 3️⃣ Insecure Temporary File
@app.route("/temp")
def insecure_temp():
    f = tempfile.mktemp()
    open(f, "w").write("temporary data")
    return "temp created"


# 4️⃣ Unsafe YAML Deserialization
@app.route("/yaml")
def yaml_load():
    data = request.data
    yaml.load(data)
    return "loaded"


# 5️⃣ Flask Debug Mode Enabled
if __name__ == "__main__":
    app.run(debug=True)