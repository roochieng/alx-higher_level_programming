#!/usr/bin/python3
"""
A model containing a Base class to manage
the id attribute of all classes that extend
from Base and avoid duplicate the same code.
"""

from os import path
import json


class Base:
    """
    This is the mother of all classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Base Class constructor
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            json_attrs = []

            for elem in list_objs:
                json_attrs.append(elem.to_dictionary())

            return f.write(cls.to_json_string(json_attrs))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Square':
            dummy = cls(3)

        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        f_name = cls.__name__ + '.json'

        if path.exists(f_name) is False:
            return []

        with open(f_name, mode='r', encoding='utf-8') as f:
            objects = cls.from_json_string(f.read())
            instances = []

            for element in objects:
                instances.append(cls.create(**element))

            return instances
