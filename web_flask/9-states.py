#!/usr/bin/python3
# Author: Joana Casallas
"""Flask Web Application to display a list of states and its cities """
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State


app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route("/states", defaults={'id_number': None}, strict_slashes=False)
@app.route("/states/<id_number>", strict_slashes=False)
def display_states(id_number):
    """ list of all State objects present in DBStorage"""
    list_states = storage.all(State).values()
    list_states = sorted(list_states, key=lambda x: x.name)
    if id_number is None:
        state_id = 0
    else:
        flag = 0
        state_id = f"{escape(id_number)}"
        state_id = state_id.strip()
        for state in list_states:
            if state.id == state_id:
                flag = 1
                break
        if flag == 0:
            state_id = 1
    return render_template('9-states.html',
                           list_states=list_states, state_id=state_id)


@app.teardown_appcontext
def close_db_connection(exception):
    """Remove the current SQLAlchemy Session after each request."""
    try:
        storage.close()
    except Exception as e:
        print(f"Error closing session:. {e}")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
