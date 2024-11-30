#!/usr/bin/python3
# Author: Joana Casallas
"""This module creates a connection with a relational database"""
import os
from sqlalchemy import create_engine
from models.base_model import Base

class DBStorage:
    """Establish a connection to the MySQL database"""
    __engine = None
    __session = None
    def __init__(self):
        """Creates the engine and session for database interaction"""
        # Retrieve environment variables
        env = os.environ.get('HBNB_ENV', 'dev')
        host = os.environ.get('HBNB_MYSQL_HOST', 'localhost')
        user = os.environ.get('HBNB_MYSQL_USER')
        password = os.environ.get('HBNB_MYSQL_PWD')
        database = os.environ.get('HBNB_MYSQL_DB')

        if not all([user, host, password, database]):
            raise ValueError("Missing environment variables for DB configuration")

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{database}',
            pool_pre_ping=True
            )
        if env == 'test':
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
