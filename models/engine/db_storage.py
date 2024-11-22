#!/usr/bin/python3
"""This module creates a connection with a relational database"""
import os
import MySQLdb

env = os.environ.get('HBNB_ENV')
host = os.environ.get('HBNB_MYSQL_HOST', 'localhost')
user = os.environ.get('HBNB_MYSQL_USER')
password = os.environ.get('HBNB_MYSQL_PWD')
database = os.environ.get('HBNB_MYSQL_DB')

if not all([host, user, password, database]):
    raise ValueError("Some required environment variables are missing")

db = MySQLdb.connect(
        host=host,
        user=user,
        passwd=password,
        db=database,
        port=3306
)
