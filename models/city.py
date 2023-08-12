#!/usr/bin/python3
""" this module contains the city class """
from models.base_model import BaseModel


class City(BaseModel):
    """ class city that inherits from the BaseModel"""
    state_id = ""
    name = ""
