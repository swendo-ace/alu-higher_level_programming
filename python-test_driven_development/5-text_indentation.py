#!/usr/bin/python3
"""Defines a text indentation function.

text_indentation(text) prints text with two newlines after each of
the characters '.', '?', and ':', trimming surrounding spaces.
"""


def text_indentation(text):
    """Print text with 2 newlines after each '.', '?', or ':'.

    Raises TypeError if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
