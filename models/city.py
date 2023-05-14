#!/usr/bin/python3
""" Defines the City Class. """
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a City
    Attributes:
        state_id (str): empty string
        name (str): empty string
    """
    
    state_id = ""
    name = ''