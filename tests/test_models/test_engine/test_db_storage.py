#!/usr/bin/python3
""" Module for testing file storage"""
import os
import unittest


class TestDBStorage(unittest.TestCase):
    """ Test cases for database connection """

    @classmethod
    def setUpClass(cls):
        """Set up environment variables and database for testing"""
        os.environ["HBNB_ENV"] = "test"
        os.environ["HBNB_MYSQL_USER"] = "test_user"
        os.environ["HBNB_MYSQL_PWD"] = "test_password"
        os.environ["HBNB_MYSQL_HOST"] = "localhost"
        os.environ["HBNB_MYSQL_DB"] = "test_db"

        # Build the absolute path dynamically
        script_dir = os.path.dirname(os.path.abspath(__file__))
        sql_file_path = os.path.join(script_dir, "../../../setup_mysql_test.sql")

        # Check if the SQL file exists
        if not os.path.exists(sql_file_path):
            raise FileNotFoundError(f"SQL file not found: {sql_file_path}")

        # Run the SQL script
        exit_code = os.system(
            f"mysql -u {os.environ['HBNB_MYSQL_USER']} "
            f"-p{os.environ['HBNB_MYSQL_PWD']} "
            f"-h {os.environ['HBNB_MYSQL_HOST']} "
            f"{os.environ['HBNB_MYSQL_DB']} < {sql_file_path}"
        )

        # Check if the command was successful
        if exit_code != 0:
            raise RuntimeError(f"Error executing SQL script. Exit code: {exit_code}")

    def test_successful_connection(self):
        """Test a successful database connection"""
        from models.engine.db_storage import get_db_connection
        connection = get_db_connection()
        self.assertIsNotNone(connection, "connection should not be None")
        connection.close()


if __name__ == "__main__":
    unittest.main()
