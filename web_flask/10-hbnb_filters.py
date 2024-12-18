#!/usr/bin/python3
# Author: Joana Casallas
"""Flask Web Application to display a list of states and its cities """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route("/hbnb_filters", strict_slashes=False)
def display_states():
    """ list of all State objects present in DBStorage"""
    list_states = storage.all(State).values()
    list_states = sorted(list_states, key=lambda x: x.name)
    print("States fetched:", list_states)
    list_amenities = storage.all(Amenity).values()
    list_amenities = sorted(list_amenities, key=lambda x: x.name)
    print("Amenities fetched:", list_amenities)
    return render_template('10-hbnb_filters.html',
                           list_states=list_states, list_amenities=list_amenities)


@app.teardown_appcontext
def close_db_connection(exception):
    """Remove the current SQLAlchemy Session after each request."""
    try:
        storage.close()
    except Exception as e:
        print(f"Error closing session:. {e}")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
