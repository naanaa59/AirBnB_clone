#!/usr/bin/python3

"""
    This class serializes instances to a JSON file
    and deserializes JSON file to instances
"""
import json
import os

class FileStorage:
    """
    attributes:
        __file_path: string - path to the JSON file
    (ex: file.json)
        __objects:  dictionary - empty but will store
    all objects by <class name>.id (ex: to store a BaseModel
    object with id=12121212, the key
    will be BaseModel.12121212)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    def save(self):
        """
        serializes __objects to the JSON file
        (path: __file_path)
        """
        serialized_objects = {}

        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open (self.__file_path, "w") as file:
            file.write(json.dumps(serialized_objects))
    
    def reload(self):
        """
        deserializes the JSON file to __objects (only if
        the JSON file (__file_path) exists
        """
        from ..base_model import BaseModel
        if os.path.exists(self.__file_path ) and os.path.getsize(self.__file_path):
            with open(self.__file_path, 'r') as file:
                deserialized_objects = json.load(file)
                for key, value in deserialized_objects.items():
                    self.__objects[key] = BaseModel(**value)

