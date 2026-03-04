from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/tpl")
def tpl():
    tpl = request.args.get("tpl")
    return render_template_string(tpl)