#!/usr/bin/python3
# Author: Joana Casallas
"""This module starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb_filters():
    """Renders a template, displaying cities, states and amenities"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    users = storage.all(User).values()
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places, users=users)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
