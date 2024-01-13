#!/usr/bin/python3
"""
    city class file
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Create a new City inheriting from BaseModel class """
    state_id = ""
    name = ""
