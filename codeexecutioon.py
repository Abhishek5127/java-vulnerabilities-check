from flask import request

def eval_exec():
    code = request.args.get("code")
    eval(code)

def exec_exec():
    code = request.args.get("code")
    exec(code)