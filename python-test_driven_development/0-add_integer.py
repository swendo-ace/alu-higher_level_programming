#!/usr/bin/python3
"""This module defines an integer addition function.

It provides add_integer(a, b), which validates that both arguments
are int or float, casts them to integers, and returns their sum.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Floats are cast to int before adding."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
