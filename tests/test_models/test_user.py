#!/usr/bin/python3
""" Module tester to check if everything is working with User class """

import unittest
import pep8
from models.user import User


class TestUser(unittest.TestCase):
    """ Tester to check if User is working as intended """

    def test_pep8(self):
        """ See if pep8 style is applied correctly """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """ Check if docstring exists """
        self.assertTrue(len(User.__doc__) > 1)
        self.assertTrue(len(User.__init__.__doc__) > 1)
        self.assertTrue(len(User.__str__.__doc__) > 1)
        self.assertTrue(len(User.save.__doc__) > 1)
        self.assertTrue(len(User.to_dict.__doc__) > 1)

    def test_init(self):
        """ Check if instance initializes """
        instance = User()
        self.assertIsInstance(instance, User)

    def test_str(self):
        """ Check if __str__ is returning correct format """
        instance = User()
        string = "[User] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(string, str(instance))

    def test_save(self):
        """ Check if save is working correctly """
        instance = User()
        instance.save()
        self.assertNotEqual(instance.created_at, instance.updated_at)

    def test_to_dict(self):
        """ Check if to_dict is returning correct format """
        instance = User()
        dictionary = instance.to_dict()
        self.assertIsInstance(dictionary, dict)
        self.assertTrue('_sa_instance_state' not in dictionary.keys())
        self.assertTrue('created_at' in dictionary.keys())
        self.assertTrue('updated_at' in dictionary.keys())
        self.assertTrue('__class__' in dictionary.keys())
        self.assertEqual(dictionary['__class__'], 'User')

if __name__ == '__main__':
    unittest.main()
    