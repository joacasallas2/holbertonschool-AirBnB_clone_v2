#!/usr/bin/python3
""" City Module for HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ Class City mapped to the cities table """
    __tablename__ = 'cities'
    if os.getenv('STORAGE_TYPE') == 'db' or os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete", passive_deletes=True)
    else:
        name =""
        state_id=""
