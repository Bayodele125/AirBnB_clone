#!/usr/bin/python
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    
    __file_path = 'file.json'
    __objects = {}
    
    def all(self):
        """Return __objects dictionary"""
        
        return FileStorage.__objects
    
    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects['{}.{}'.format(obj_class_name,obj.id )] = obj
        
    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)
        """
        
        object = FileStorage.__objects
        obj_dict = {obj: object[obj].to_dict() for obj in object}
        
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)
            
    def reload(self):
        """ deserializes the JSON file to __objects, if it exists"""
        
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return