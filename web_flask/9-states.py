#!/usr/bin/python3
# Author: Joana Casallas
"""Flask Web Application to display a list of states and its cities """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", defaults={'state_id': None}, strict_slashes=False)
@app.route("/states/<state_id>", strict_slashes=False)
def display_states(state_id):
    """ list of all State objects present in DBStorage"""
    dict_states = storage.all(State).values()
    dict_states = sorted(dict_states, key=lambda x: x.name)
    return render_template('9-states.html',
                           dict_states=dict_states, state_id=state_id)


@app.teardown_appcontext
def close_db_connection(exception):
    """Remove the current SQLAlchemy Session after each request."""
    try:
        storage.close()
    except Exception as e:
        print(f"Error closing session:. {e}")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
