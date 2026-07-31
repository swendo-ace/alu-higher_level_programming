#!/usr/bin/python3
"""Defines an inherits_from function."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a strict subclass of a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
