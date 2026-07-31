#!/usr/bin/python3
"""Defines a write_file function."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file, returning chars written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
