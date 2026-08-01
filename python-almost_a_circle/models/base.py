#!/usr/bin/python3
"""Defines the Base class for all other classes in the project."""
import json


class Base:
    """Base class managing the id attribute for all subclasses."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id: the identity of the new instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string of a list of objects to a file."""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
