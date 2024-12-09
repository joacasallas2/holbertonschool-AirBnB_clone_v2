#!/usr/bin/python3
# Author: Joana Casallas
"""Flask Web Application to display a list of states and its cities """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_state():
    """Display a HTML page with the list of cities by state"""
    dict_states = storage.all(State)
    dict_cities = storage.all(City)
    list_states = sorted(list(dict_states.values()), key=lambda x: x.name)
    state_with_cities = []
    for state in list_states:
        list_cities = [
            city for city in dict_cities.values() if city.state_id == state.id]
        list_cities = sorted(list_cities, key=lambda x: x.name)
        state_with_cities.append((state, list_cities))
        list_cities = []
    return render_template(
        '8-cities_by_states.html', state_with_cities=state_with_cities)


@app.teardown_appcontext
def close_db_connection(exception):
    """Remove the current SQLAlchemy Session after each request."""
    try:
        storage.close()
    except Exception as e:
        print(f"Error closing session:. {e}")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
