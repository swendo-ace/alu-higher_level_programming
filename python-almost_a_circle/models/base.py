#!/usr/bin/python3
"""Defines the Base class for all other classes in the project."""


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
