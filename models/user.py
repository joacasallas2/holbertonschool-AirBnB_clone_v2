#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """User class mapped to the users table"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place",
                          backref="user",
                          cascade="all, delete, delete-orphan",
                          passive_deletes=True)
    reviews = relationship("Review",
                           backref="user",
                           cascade="all, delete, delete-orphan",
                           passive_deletes=True)
