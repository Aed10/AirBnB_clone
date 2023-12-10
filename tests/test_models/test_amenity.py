#!/usr/bin/python3
""" Module tester to check if everything is working with Amenity class """

import unittest
import pep8
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Tester to check if Amenity is working as intended """

    def test_pep8(self):
        """ See if pep8 style is applied correctly """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """ Check if docstring exists """
        self.assertTrue(len(Amenity.__doc__) > 1)
        self.assertTrue(len(Amenity.__init__.__doc__) > 1)
        self.assertTrue(len(Amenity.__str__.__doc__) > 1)
        self.assertTrue(len(Amenity.save.__doc__) > 1)
        self.assertTrue(len(Amenity.to_dict.__doc__) > 1)

    def test_init(self):
        """ Check if instance initializes """
        instance = Amenity()
        self.assertIsInstance(instance, Amenity)

    def test_str(self):
        """ Check if __str__ is returning correct format """
        instance = Amenity()
        string = "[Amenity] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(string, str(instance))

    def test_save(self):
        """ Check if save is working correctly """
        instance = Amenity()
        instance.save()
        self.assertNotEqual(instance.created_at, instance.updated_at)

    def test_to_dict(self):
        """ Check if to_dict is returning correct format """
        instance = Amenity()
        dictionary = instance.to_dict()
        self.assertIsInstance(dictionary, dict)
        self.assertTrue('_sa_instance_state' not in dictionary.keys())
        self.assertTrue('created_at' in dictionary.keys())
        self.assertTrue('updated_at' in dictionary.keys())
        self.assertTrue('__class__' in dictionary.keys())
        self.assertEqual(dictionary['__class__'], 'Amenity')

if __name__ == '__main__':
    unittest.main()