#!/usr/bin/python3
"""This moddule to test the state class"""
import unittest
import pep8
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """This class to test the state class"""

    def test_pep8_conformance(self):
        """Test that we conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        """Test that class is named correctly"""
        state1 = State()
        state1.name = "Test State"
        self.assertEqual(state1.__class__.__name__, "State")

    def test_father(self):
        """Test that class inherits from BaseModel"""
        state1 = State()
        self.assertTrue(issubclass(state1.__class__, BaseModel))

    def test_attributes(self):
        """Test that class has place_id, user_id and text attributes"""
        state1 = State()
        self.assertTrue("name" in state1.__dict__)

    def test_to_dict(self):
        """Test to_dict method"""
        state1 = State()
        state1_dict = state1.to_dict()
        self.assertTrue("__class__" in state1_dict)
        self.assertTrue("created_at" in state1_dict)
        self.assertTrue("updated_at" in state1_dict)
        self.assertTrue('id' in state1_dict)

    def test_str(self):
        """Test __str__ method"""
        state1 = State()
        string = "[State] ({}) {}".format(state1.id, state1.__dict__)
        self.assertEqual(string, str(state1))

if __name__ == "__main__":
    unittest.main()
    