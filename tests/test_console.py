"""Tests"""

import unittest
import os
from io import StringIO
from unittest.mock import patch
import pep8
from models import storage
from console import HBNBCommand
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    """Group of tests of HBNBCommand class"""

    def setUp(self):
        """initialize conditions to each test"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up conditions after each test"""
        storage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_pep8_HBNBCommand(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['console.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_quit(self):
        """Test of HBNBCommand class for the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertEqual("", f.getvalue())

    def test_EOF(self):
        """Test of HBNBCommand class for the EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("EOF")
            self.assertTrue(self.console.onecmd("EOF"))

    def test_emptyline(self):
        """Test of HBNBCommand class for the emptyline command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)


if __name__ == "__main__":
    unittest.main()
