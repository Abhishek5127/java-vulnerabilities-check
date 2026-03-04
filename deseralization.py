from flask import Flask, request
import pickle
import yaml

app = Flask(__name__)

@app.route("/pickle")
def pickle_load():
    data = request.data
    pickle.loads(data)
    return "ok"

@app.route("/yaml")
def yaml_load():
    data = request.data
    yaml.load(data)
    return "ok"