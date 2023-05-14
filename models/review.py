#!/usr/bin/python3
""" Defines the Review Class. """
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a Review
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): empty string
    """
    
    place_id = ''
    user_id = ''
    text = ''