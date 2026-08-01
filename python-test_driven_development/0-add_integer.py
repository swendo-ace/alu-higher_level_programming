#!/usr/bin/python3
"""Defines an integer addition function.

add_integer(a, b=98) adds two numbers after validating that both
are int or float, casting floats to integers before adding.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Raises TypeError if a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
