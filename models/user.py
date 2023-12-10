#!/usr/bin/python3
"""This module defines a User Model"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a User by various attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """This method initializes a User instance"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """This method prints a string representation of a User instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
