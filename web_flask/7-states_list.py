#!/usr/bin/python3
# Author: Joana Casallas
"""This module starts a Flask web application:"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """display a HTML page with the states info"""
    dict_states = storage.all(State)
    states = dict_states.values()
    return render_template('7-states_list.html',  states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
