#!/usr/bin/python3
"""
Module: __init__.py module
"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
