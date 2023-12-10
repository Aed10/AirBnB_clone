#!/usr/bin/pythin3
"""Unittest for FileStorage class"""
import unittest
import pep8
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up test methods"""
        self.file = FileStorage()

    def tearDown(self):
        """Tear down test methods"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8(self):
        """Check pep8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """Check docstring"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_docmodule(self):
        """Check module docstring"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_instance(self):
        """Check instance"""
        self.assertIsInstance(self.file, FileStorage)

    def test_all(self):
        """Check all"""
        self.assertEqual(self.file.all(), {})

    def test_new(self):
        """Check new"""
        self.file.new(BaseModel())
        self.assertEqual(len(self.file.all()), 1)

    def test_save(self):
        """Check save"""
        self.file.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Check reload"""
        self.file.save()
        self.file.reload()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_empty(self):
        """Check reload empty"""
        self.file.reload()
        self.assertEqual(self.file.all(), {})

    def test_reload_from_nonexistent(self):
        """Check reload from nonexistent"""
        self.file.save()
        os.remove("file.json")
        self.file.reload()
        self.assertEqual(self.file.all(), {})

    def test_reload_from_corrupted(self):
        """Check reload from corrupted"""
        self.file.save()
        with open("file.json", "w") as f:
            f.write("Hello")
        self.file.reload()
        self.assertEqual(self.file.all(), {})

    def test_reload_from_empty(self):
        """Check reload from empty"""
        with open("file.json", "w") as f:
            f.write("")
        self.file.reload()
        self.assertEqual(self.file.all(), {})

    def test_reload_from_non_json(self):
        """Check reload from non json"""
        with open("file.json", "w") as f:
            f.write("Hello")
        self.file.reload()
        self.assertEqual(self.file.all(), {})