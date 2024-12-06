#!/usr/bin/python3
# Author: Joana Casallas
"""script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """display hello"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """display c text"""
    sentence = f"c {escape(text)}"
    sentence = sentence.replace("_", " ")
    return sentence


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Display Python text"""
    sentence = f"python {escape(text)}"
    sentence = sentence.replace("_", " ")
    return sentence


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
