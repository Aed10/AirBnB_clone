#!/usr/bin/python3
"""This moddule to test the city class"""
import unittest
import pep8
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """This class to test the city class"""

    def test_pep8_conformance(self):
        """Test that we conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        """Test that class is named correctly"""
        city1 = City()
        city1.name = "Test City"
        self.assertEqual(city1.__class__.__name__, "City")

    def test_father(self):
        """Test that class inherits from BaseModel"""
        city1 = City()
        self.assertTrue(issubclass(city1.__class__, BaseModel))

    def test_attributes(self):
        """Test that class has place_id, user_id and text attributes"""
        city1 = City()
        self.assertTrue("name" in city1.__dict__)
        self.assertTrue("state_id" in city1.__dict__)

    def test_to_dict(self):
        """Test to_dict method"""
        city1 = City()
        city1_dict = city1.to_dict()
        self.assertTrue("__class__" in city1_dict)
        self.assertTrue("created_at" in city1_dict)
        self.assertTrue("updated_at" in city1_dict)
        self.assertTrue('id' in city1_dict)

    def test_str(self):
        """Test __str__ method"""
        city1 = City()
        string = "[City] ({}) {}".format(city1.id, city1.__dict__)
        self.assertEqual(string, str(city1))

if __name__ == "__main__":
    unittest.main()
