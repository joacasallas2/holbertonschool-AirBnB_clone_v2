#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class DBStorage:
    """class DBStorage to manage a mysql Database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize mysql database connection"""
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        database = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{passwd}@{host}/{database}',
            pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in database session"""
        dict_objs = {}
        list_classes = []
        dict_classes = {
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review}
        if cls is None:
            list_classes = dict_classes.values()
        else:
            if isinstance(cls, str):
                cls = dict_classes[cls]
            list_classes = [cls]
        for cls in list_classes:
            try:
                objs_by_class = self.__session.query(cls).all()
                for obj in objs_by_class:
                    k = f"{obj.__class__.__name__}.{obj.id}"
                    v = obj
                    dict_objs[k] = v
            except KeyError as e:
                print("Error: cls {cls} doesn't exists")
        return dict_objs
