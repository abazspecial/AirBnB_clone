#!/usr/bin/python3
""" The Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ The Review class to store review information """
    place_id = ""
    user_id = ""
    text = ""
