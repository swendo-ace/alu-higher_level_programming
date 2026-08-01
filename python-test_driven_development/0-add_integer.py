#!/usr/bin/python3
"""Defines an integer addition function.

This module provides a single function, add_integer, which safely
adds two numbers after validating and casting them to integers.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Args:
        a: the first number (int or float)
        b: the second number (int or float, default 98)

    Raises:
        TypeError: if a or b is not an int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
