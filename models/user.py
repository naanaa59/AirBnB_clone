#!/usr/bin/python3
"""
    User class file this class inheartes from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Create a new User inheriting from BaseModel class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
