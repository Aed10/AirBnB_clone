#!/usr/bin/python3
"""This module defines a Review class"""
from models.base_model import BaseModel


class Review(BaseModel):

    """This class defines a Review by various attributes"""
    place_id = ""
    user_id = ""
    text = ""
