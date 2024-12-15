#!/usr/bin/python3
# Author: Joana Casallas
"""Flask Web Application to display a list of states and its cities """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_state():
    """Display a HTML page with the list of cities by state"""
    dict_states = storage.all(State).values()
    return render_template(
        '8-cities_by_states.html', dict_states=dict_states)


@app.teardown_appcontext
def close_db_connection(exception):
    """Remove the current SQLAlchemy Session after each request."""
    try:
        storage.close()
    except Exception as e:
        print(f"Error closing session:. {e}")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
