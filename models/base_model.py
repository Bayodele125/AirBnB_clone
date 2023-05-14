#!/usr/bin/python3
import models
import uuid
from datetime import datetime

class BaseModel:
    """Represents the BaseModel of the HBnB project."""
    
    def __init__(self, *args, **kwargs):
        """Initailize a new BaseModel.
        
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        
        if kwargs != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated":
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)    
                    
    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()
        
    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
        
        
    def __str__(self) -> str:
        """Return the str representation of the BaseModel instance."""
        c_name = self.__class__.__name__
        return "[<{}>] (<{}>) <{}>".format(c_name, self.id, self.__dict__)
