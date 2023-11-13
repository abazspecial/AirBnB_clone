#!/usr/bin/python3
"""The `amenity` module

this is the module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """An amenity provided by a place/house.

    Attributes:
        name
    """

    name = ""
