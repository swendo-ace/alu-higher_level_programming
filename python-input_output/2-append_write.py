#!/usr/bin/python3
"""Defines an append_write function."""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF-8 text file, returning chars added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
