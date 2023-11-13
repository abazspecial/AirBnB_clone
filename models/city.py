#!/usr/bin/python3
""" this is the City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """City class, contains state ID and name """
    state_id = ""
    name = ""
