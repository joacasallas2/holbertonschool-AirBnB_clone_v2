#!/usr/bin/python3
""" Module for testing file storage"""
import os
import unittest
from models.engine.db_storage import get_db_connection


class TestDBStorage(unittest.TestCase):
    """ Test cases for database connection """

    @classmethod
    def setUpClass(cls):
        """Set up environment variables for testing"""
        os.environ["HBNB_ENV"] = "test"
        os.environ["HBNB_MYSQL_USER"] = "test_user"
        os.environ["HBNB_MYSQL_PWD"] = "test_password"
        os.environ["HBNB_MYSQL_HOST"] = "localhost"
        os.environ["HBNB_MYSQL_DB"] = "test_db"
        os.system("../setup_mysql_test")

    def test_successful_connection(self):
        """test a successful database connection"""
        connection = get_db_connection()
        self.assertIsNotNone(connection, "connection should not be None")
        connection.close()


if __name__ == "__main__":
    unittest.main()
