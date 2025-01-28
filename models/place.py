#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place', cascade='all, delete-orphan')
    else:
        @property
        def reviews(self):
            """get the list of reviews with the same place_id"""
            from models import storage
            from models.review import Review
            dict_objs = storage.all(Review)
            list_reviews_instance = []
            for obj in dict_objs.values():
                if obj.place_id == self.id:
                    list_reviews_instance.append(obj)
            return list_reviews_instance
