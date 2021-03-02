from application import app
from flask import render_template, request, redirect


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return 'test'


@app.route("/api", methods=['POST'])
def message_handler():
    if request.method == 'POST':
        return None
    return None


