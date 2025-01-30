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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def text_python(text="is cool"):
    """Complete a sentence with the parameter"""
    if "_" in text:
        text = text.replace("_", " ")
    return f"Python {escape(text)}"


@app.route("/number/<int:n>", strict_slashes=False)
def if_number(n):
    """display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return f"{escape(n)} is a number"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
