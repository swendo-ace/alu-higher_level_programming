#!/usr/bin/python3
"""Defines the Square class, inheriting from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size: the size (used as both width and height)
            x: the x position
            y: the y position
            id: the identity (passed to Base)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size (width)."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size, assigning width then height."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes via args (ordered) or kwargs (named).

        Args:
            *args: id, size, x, y (in order)
            **kwargs: attribute names and values (skipped if args given)
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Return the square description."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
