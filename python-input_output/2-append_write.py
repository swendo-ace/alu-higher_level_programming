#!/usr/bin/python3
"""Defines an append_write function."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 file and return chars added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
