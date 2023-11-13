#!/usr/bin/python3
"""This particular module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This particular class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
