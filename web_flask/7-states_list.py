#!/usr/bin/python3
# Author: Joana Casallas
"""Flask Web Application to display a list of states """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list_function():
    """Display a HTML page with the list of states"""
    dict_objs = storage.all(State)
    states_list = sorted(list(dict_objs.values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states_list=states_list)


@app.teardown_appcontext
def close_db_connection(exception):
    """Remove the current SQLAlchemy Session after each request."""
    try:
        storage.close()
    except Exception as e:
        print(f"Error closing session:. {e}")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
