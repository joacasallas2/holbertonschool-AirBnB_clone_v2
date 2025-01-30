#!/usr/bin/python3
# Author: Joana Casallas
"""This module starts a Flask web application:"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """return hello"""
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
