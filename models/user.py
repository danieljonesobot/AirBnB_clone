#!/usr/bin/python3

"""this module defines the class called User which inherits from
parent class BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """class the to initialize a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
