#!/usr/bin/python3
# Author: Joana Casallas
"""This module starts a Flask web application:"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text_c(text):
    """Complete a sentence with the parameter"""
    if "_" in text:
        text = text.replace("_", " ")
    return f"C {escape(text)}"



def sentence_python():
    """Display Python is cool"""
    return "Python is cool"

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def text_python(text="is cool"):
    """Complete a sentence with the parameter"""
    if "_" in text:
        text = text.replace("_", " ")
    return f"Python {escape(text)}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
