#!/usr/bin/python
# Author: Joana Casallas
""" script that starts a Flask web application """
from flask import Flask


app = Flask(__name__)


@app.route("/")
def Hello():
    """ function that display Hello HBNB"""
    return "<p>Hello HBNB!</p>"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
