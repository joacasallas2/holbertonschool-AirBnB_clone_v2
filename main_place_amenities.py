#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import (state, city, place, user, amenity)
from models.__init__ import storage



# creation of a State
state = state.State(name="California")
state.save()
