#!/usr/bin/python3
"""This module defines a class to connect a mysql database for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """This class connect the mysql database"""
    __engine = None
    __session = None

    def __init__(self):
        """Create connection with the database"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_TYPE_STORAGE')

        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{db}",
            pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Return a dictionary with all objects in the storage
        depending of the class name"""
        dict_objs = {}
        list_classes = []
        if cls is None:
            list_classes = Base.__subclasses__()
        else:
            if isinstance(cls, str):
                cls = next(
                    (c for c in list_classes if c.__name__ == cls), None)
                if cls is None:
                    return dict_objs
            list_classes = [cls]
        for cls_name in list_classes:
            objects_class = self.__session.query(cls_name).all()
            for obj in objects_class:
                key = f"{cls_name.__name__}.{obj.id}"
                obj_dict = obj.__dict__.copy()
                obj_dict.pop('_sa_instance_state', None)
                dict_objs[key] = obj
        return dict_objs

    def new(self, obj):
        """add the object to the database"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes"""
        try:
            self.__session.commit()
        except Exception as e:
            print(f"Unable to save changes: {e}")
            self.__session.rollback()
            raise e

    def delete(self, obj=None):
        """Delete obj from the database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create the database and its tables"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """close method in DBstorage"""
        if self.__session:
            self.__session.remove()
