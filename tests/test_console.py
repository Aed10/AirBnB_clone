#!/usr/bin/python3
"""This moddule to test the console class"""
import unittest
import pep8
from unittest.mock import patch

from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """This class to test the console class"""

    def test_pep8_conformance(self):
        """Test that we conforms to PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring(self):
        """Test that docstring exists"""
        self.assertTrue(len(HBNBCommand.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_quit.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_EOF.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.emptyline.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_create.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_show.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_destroy.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_all.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_update.__doc__) > 1)

    def test_emptyline(self):
        """Test emptyline method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_quit(self):
        """Test quit method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual("", f.getvalue())

    def test_EOF(self):
        """Test EOF method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual("", f.getvalue())

    def test_create(self):
        """Test create method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create asdf")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue()) > 0)

    def test_show(self):
        """Test show method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show asdf")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1234-1234-1234")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_destroy(self):
        """Test destroy method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy asdf")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1234-1234-1234")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_all(self):
        """Test all method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all asdf")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertTrue(len(f.getvalue()) > 0)

    def test_update(self):
        """Test update method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update asdf")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1234-1234-1234")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1234-1234-1234 asdf")
            self.assertEqual("** value missing **\n", f.getvalue())

if __name__ == "__main__":
    unittest.main()