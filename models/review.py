#!/usr/bin/python3
""" this module defines the reivew class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ this class represents a review.
    """

    place_id = ""
    user_id = ""
    text = ""
