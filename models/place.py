#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


place_amenity = Table('place_amenity', Base.metadata,
                      Column(
                          'place_id',
                          String(60),
                          ForeignKey('places.id'),
                          primary_key=True,
                          nullable=False),
                      Column(
                          'amenity_id',
                          String(60),
                          ForeignKey('amenities.id'),
                          primary_key=True,
                          nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            'Review', backref='place', cascade='all, delete-orphan')
        amenities = relationship('Amenity',
                                 secondary='place_amenity',
                                 back_populates='place_amenities',
                                 viewonly=False)
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

        @property
        def amenities(self):
            """Get the list of amenities with the same place_id"""
            from models import storage
            from models.amenity import Amenity
            list_amenities = storage.all(Amenity).values()
            list_amenities_instance = []
            for amenity in list_amenities:
                if amenity.id in self.amenity_ids:
                    list_amenities_instance.append(amenity)
            return list_amenities_instance

        @amenities.setter
        def amenities(self, amenity):
            """Set (append) amenities to the list with the same place_id"""
            from models.amenity import Amenity
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
