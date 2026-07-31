#!/usr/bin/python3
"""Defines a Student class with serialization and deserialization."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name: the student's first name
            last_name: the student's last name
            age: the student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dict of the Student, optionally filtered by attrs.

        Args:
            attrs: an optional list of attribute names to include
        """
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student from a dictionary.

        Args:
            json: a dictionary of attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
