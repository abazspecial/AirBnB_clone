#!/usr/bin/python3
"""The `review` module.

This  defines one class, `Review(),
which sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A review of a place/house.

    It represents a review posted by the users
    of the application about a place/house.

    """
    text = ""
    user_id = ""
    place_id = ""
