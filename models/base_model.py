#!usr/bin/python3
"""Module creates a super class ``BaseModel`` to define all common attributes
and methods for other classes in the project"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    '''class defines common attributes and methods for other classes'''
    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif not key == '__class__':
                    setattr(self, key, value)

    def __str__(self):
        cls_nm = self.__class__.__name__
        obj_id = self.id
        obj_dct = self.__dict__
        return f"[{cls_nm}] ({obj_id}) {obj_dct}"

    def save(self):
        '''instance method to update public attribute [updated_at] with current
        datetime'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''instance method returns a dictionary with keys/values of __dict__
        of the instance'''
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
