#!/usr/bin/python3
# Author: Joana Casallas
"""This module starts a Flask web application"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id_num>", strict_slashes=False)
def states_and_state(id_num=None):
    """Display all cities of a State"""
    states = storage.all(State).values()
    state = None
    if id_num:
        id_num = escape(id_num)
        for obj in states:
            if obj.id == id_num:
                state = obj
    return render_template(
        '9-states.html',  states=states, id_num=id_num, state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
