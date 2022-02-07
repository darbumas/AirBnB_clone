#!/usr/bin/python3
"""
The Review subclass of BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    The Review subclass of BaseModel.
    """
    place_id = ""
    user_id = ""
    text = ""
