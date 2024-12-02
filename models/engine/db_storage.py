#!/usr/bin/python3
# Author: Joana Casallas
"""This module creates a connection with a relational database"""
import os
from sqlalchemy.orm import sessionmaker, scoped_session
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

    def __init__(self):
        """Initialize the engine and session for database connection"""
        from models.base_model import Base
        from sqlalchemy import create_engine
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
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def all(self, cls=None):
        """Query all objects on the current database session"""
        if cls is None:
            classes = [State, City]
        else:
            if isinstance(cls, str):
                cls = globals().get(cls)
            classes = [cls]

        objects = {}
        for class_type in classes:
            query = self.__session.query(class_type).all()
            for obj in query:
                key = f"{obj.__class__.__name__}.{obj.id}"
                objects[key] = obj
        return objects

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        try:
            self.__session.commit()
        except Exception:
            self.__session.rollback()

    def delete(self, obj=None):
        """Delete obj from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create tables and create the current session"""
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
