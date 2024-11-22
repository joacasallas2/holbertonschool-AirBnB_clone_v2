#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Testing review """

    def __init__(self, *args, **kwargs):
        """ Initialize data """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Testing place_id """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Testing user_id """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Testing text """
        new = self.value()
        self.assertEqual(type(new.text), str)
