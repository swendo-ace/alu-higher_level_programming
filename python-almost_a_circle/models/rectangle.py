#!/usr/bin/python3
"""Defines the Rectangle class, inheriting from Base."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle, inheriting from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width: the width of the rectangle
            height: the height of the rectangle
            x: the x position
            y: the y position
            id: the identity (passed to Base)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width."""
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height."""
        self.__height = value

    @property
    def x(self):
        """Get x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x."""
        self.__x = value

    @property
    def y(self):
        """Get y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y."""
        self.__y = value
