#!/usr/bin/python3
""" Module for testing DBStorage"""
import unittest
from models.state import State
from models import storage


class TestDBStorage(unittest.TestCase):
    """Class to test the DBStorage methods"""

    def setUp(self):
        """Clean database after each test"""
        self.storage = storage
        for obj in self.storage.all().values():
            self.storage.delete(obj)
        self.storage.save()

    def tearDown(self):
        """Ensure database is clean after each test"""
        for obj in self.storage.all().values():
            self.storage.delete(obj)
        self.storage.save()

    @classmethod
    def setUpClass(cls):
        """Set up for DBStorage tests"""
        cls.storage = storage
        cls.storage.reload()

    def test_all_returns_dict(self):
        """Test that all returns a dictionary"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_adds_object(self):
        """Test that new adds an object to the database"""
        new_state = State(name="California")
        self.storage.new(new_state)
        self.storage.save()
        self.assertIn(f"State.{new_state.id}", self.storage.all())

    def test_reload_loads_objects(self):
        """Test that reload loads objects from the database"""
        new_state = State(name="Florida")
        self.storage.new(new_state)
        self.storage.save()
        self.storage.reload()
        self.assertIn(f"State.{new_state.id}", self.storage.all())


if __name__ == "__main__":
    unittest.main()
