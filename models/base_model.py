#!/usr/bin/env python3
"""
    This class named BaseModel that defines all common attributes/methods
    for other classes
"""


import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
        Public Attributes:
            id : UUID4 generated ad converted to string
            created_at : datetime assign when instance created
            updated_at : datetime assign when instance updated

        Public Methods:
            save(self): updates the instance attribute
                        updated_at with current datetime
            to_dict(self): returns a dictionary with all keys/values
    """
    def __init__(self, *args, **kwargs):
        """
            Initialization method for att attributes
            we can create an instance with kwargs or without
            args
        """
        if kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
            prints [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
            updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
