#!/usr/bin/python3
"""Defines a square-printing function.

print_square(size) prints a square of # characters after validating
that size is a non-negative integer.
"""


def print_square(size):
    """Print a square of side length size using the # character.

    Raises TypeError if size is not an integer,
    ValueError if size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
