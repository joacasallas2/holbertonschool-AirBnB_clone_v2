#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from datetime import datetime


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        dict_objs = {}
        for k, v in self.__objects.items():
            if k.split(".")[0] == cls.__name__:
                dict_objs[k] = v
        return dict_objs


    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                try:
                    temp = json.load(f)
                    for key, val in temp.items():
                        if 'created_at' in val:
                            if isinstance(val['created_at'], str):
                                val['created_at'] = datetime.strptime(
                                    val['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                        if 'updated_at' in val:
                            if isinstance(val['updated_at'], str):
                                val['updated_at'] = datetime.strptime(
                                    val['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                        self.all()[key] = classes[val['__class__']](**val)
                except json.JSONDecodeError:
                    pass
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete an object from the storage"""
        if obj is None:
            return
        for key in self.__objects:
            if key.split(".")[1] == obj.id:
                del self.__objects[key]
                break
