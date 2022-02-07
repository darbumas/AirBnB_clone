#!/usr/bin/python3
"""
The User subclass inherited from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    The User subclass of BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
