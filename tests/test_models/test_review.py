#!/usr/bin/python3
"""This moddule to test the review class"""
import unittest
import pep8
from models.review import Review


class TestReview(unittest.TestCase):
    """This class to test the review class"""

    def test_pep8_conformance(self):
        """Test that we conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        """Test that class is named correctly"""
        review1 = Review()
        review1.name = "Test Review"
        self.assertEqual(review1.__class__.__name__, "Review")

    def test_attributes(self):
        """Test that class has place_id, user_id and text attributes"""
        review1 = Review()
        self.assertTrue("place_id" in review1.__dict__)
        self.assertTrue("user_id" in review1.__dict__)
        self.assertTrue("text" in review1.__dict__)

    def test_to_dict(self):
        """Test to_dict method"""
        review1 = Review()
        review1_dict = review1.to_dict()
        self.assertTrue("__class__" in review1_dict)
        self.assertTrue("created_at" in review1_dict)
        self.assertTrue("updated_at" in review1_dict)
        self.assertTrue('id' in review1_dict)

    def test_str(self):
        """Test __str__ method"""
        review1 = Review()
        string = "[Review] ({}) {}".format(review1.id, review1.__dict__)
        self.assertEqual(string, str(review1))

if __name__ == "__main__":
    unittest.main()
