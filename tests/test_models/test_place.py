#!/usr/bin/python3
""" Module tester to check if everything is working with place class """

import unittest
import pep8
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Tester to check if Place is working as intended """

    def test_pep8(self):
        """ See if pep8 style is applied correctly """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """ Check if docstring exists """
        self.assertTrue(len(Place.__doc__) > 1)
        self.assertTrue(len(Place.__init__.__doc__) > 1)
        self.assertTrue(len(Place.__str__.__doc__) > 1)
        self.assertTrue(len(Place.save.__doc__) > 1)
        self.assertTrue(len(Place.to_dict.__doc__) > 1)

    def test_init(self):
        """ Check if instance initializes """
        instance = Place()
        self.assertIsInstance(instance, Place)

    def test_str(self):
        """ Check if __str__ is returning correct format """
        instance = Place()
        string = "[Place] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(string, str(instance))

    def test_save(self):
        """ Check if save is working correctly """
        instance = Place()
        instance.save()
        self.assertNotEqual(instance.created_at, instance.updated_at)

    def test_to_dict(self):
        """ Check if to_dict is returning correct format """
        instance = Place()
        dictionary = instance.to_dict()
        self.assertIsInstance(dictionary, dict)
        self.assertTrue('_sa_instance_state' not in dictionary.keys())
        self.assertTrue('created_at' in dictionary.keys())
        self.assertTrue('updated_at' in dictionary.keys())
        self.assertTrue('__class__' in dictionary.keys())
        self.assertEqual(dictionary['__class__'], 'Place')

if __name__ == '__main__':
    unittest.main()
    