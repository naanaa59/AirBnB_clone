#!/usr/bin/python3
"""
    Review class file
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Create a new User inheriting from BaseModel class """
    place_id = ""
    user_id = ""
    text = ""
