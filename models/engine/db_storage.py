#!/usr/bin/python3
"""This module creates a connection with a relational database"""
import os
import MySQLdb

def get_db_connection():
    """ Establish a connection to the MySQL database """
    env = os.environ.get('HBNB_ENV', 'dev')
    host = os.environ.get('HBNB_MYSQL_HOST', 'localhost')
    user = os.environ.get('HBNB_MYSQL_USER')
    password = os.environ.get('HBNB_MYSQL_PWD')
    database = os.environ.get('HBNB_MYSQL_DB')

    if not all([host, user, password, database]):
        raise ValueError("Some required environment variables are missing")

    if env == 'test':
        database = f"{database}_test"

    try:
        db = MySQLdb.connect(
            host=host,
            user=user,
            passwd=password,
            db=database,
            port=3306
        )
        print("Database connection established successfully.")
        return db
    except MySQLdb.OperationalError as e:
        print(f"Error connecting to MySQL: {e}")
        return None

if __name__ == "__main__":
    connection = get_db_connection()
    if connection:
        connection.close()
