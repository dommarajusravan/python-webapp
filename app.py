from flask import Flask
app = Flask(__name__)

@app.route("/")
def webapp():
    return "<h1>The saved string is dynamic string</h1>"
