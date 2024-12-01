#!/usr/bin/python3
# Author: Joana Casallas
"""This module creates a connection with a relational database"""
import os
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User


class DBStorage:
    """Database Storage engine for MySQL database"""

    __engine = None
    __session = None
    __class_names = {User, State, City, Amenity, Place, Review}

    def __init__(self):
        """Initialize the engine and session for database connection"""
        # Retrieve environment variables
        env = os.environ.get("HBNB_ENV", "dev")
        host = os.environ.get("HBNB_MYSQL_HOST", "localhost")
        user = os.environ.get("HBNB_MYSQL_USER")
        password = os.environ.get("HBNB_MYSQL_PWD")
        database = os.environ.get("HBNB_MYSQL_DB")

        if not all([user, host, password, database]):
            raise ValueError("Missing environment variables for DB configuration")

        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{database}", pool_pre_ping=True
        )
        if env == "test":
            try:
                connection = self.__engine.connect()
                connection.execute("SET FOREIGN_KEY_CHECKS = 0")
                result = connection.execute(
                    "SELECT table_name FROM information_schema.tables WHERE table_schema = DATABASE();"
                )
                for row in result:
                    table_name = row[0]
                    connection.execute(f"DROP TABLE IF EXISTS `{table_name}`;")
            except Exception as e:
                print(f"Error while dropping tables; {e}")
            finally:
                connection.close()
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        """Query all objects on the current database session"""
        dict_objs = {}
        if cls is None:
            for class_name in self.__class_names:
                query_results = self.__session.query(class_name).all()
                for obj in query_results:
                    key = f"{type(obj).__name__}.{obj.id}"
                    dict_objs[key] = obj
        else:
            if cls in self.__class_names:
                query_results = self.__session.query(cls).all()
                for obj in query_results:
                    key = f"{type(obj).__name__}.{obj.id}"
                    dict_objs[key] = obj
            else:
                raise ValueError(f"Class {cls} is not recognized")
        return dict_objs
