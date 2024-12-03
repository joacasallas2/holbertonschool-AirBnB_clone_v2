#!/usr/bin/python3
""" City Module for HBNB project """
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """User class mapped to the users table"""
    __tablename__ = 'users'
    if os.getenv('STORAGE_TYPE') == 'db' or os.getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user", cascade="all, delete", passive_deletes=True)
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
