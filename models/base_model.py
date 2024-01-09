#!/usr/bin/env python3
"""
    This class named BaseModel that defines all common attributes/methods
    for other classes
"""


import uuid
from datetime import datetime


class BaseModel():
    """
        Public Attributes:
            id : UUID4 generated ad converted to string
            name : The name of the model
            my_number : The number of the model
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
        """
        if kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    self.__dict__.update({key: value})
            self.created_at = datetime.fromisoformat(str(kwargs.get('created_at')))
            self.updated_at = datetime.fromisoformat(str(kwargs.get('updated_at')))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

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

    def to_dict(self):
        """
            returns a dictionary containing all keys/values
        """
        dictionary = self.__dict__
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary










