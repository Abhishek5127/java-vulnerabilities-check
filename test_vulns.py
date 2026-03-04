from flask import Flask, request
import os
import subprocess

app = Flask(__name__)

@app.route("/os")
def os_cmd():
    cmd = request.args.get("cmd")
    os.system(cmd)
    return "done"

@app.route("/subprocess")
def subprocess_cmd():
    cmd = request.args.get("cmd")
    subprocess.call(cmd, shell=True)
    return "done"

@app.route("/popen")
def popen_cmd():
    cmd = request.args.get("cmd")
    os.popen(cmd)
    return "done"

if __name__ == "__main__":
    app.run()