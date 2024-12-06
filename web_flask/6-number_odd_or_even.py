#!/usr/bin/python3
# Author: Joana Casallas
"""script that starts a Flask web application"""
from flask import Flask, render_template
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
    sentence = f"Python {escape(text)}"
    sentence = sentence.replace("_", " ")
    return sentence


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display n is a number only if n is integer"""
    return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """display template only if n is a number"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """display template only if n in a number"""
    even_number = "even"
    if n % 2 != 0:
        even_number = "odd"
    return render_template('6-number_odd_or_even.html', n=n, even_number=even_number)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
