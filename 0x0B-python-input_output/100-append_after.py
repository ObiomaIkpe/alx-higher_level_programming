#!/usr/bin/python3
"""Defines a function ``append_after``"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a linew of text to a file, after each line containing
    a specific string

    Args:
        filename (str): name of file
        search_string (str): string to be searched for
        new_string (str): string to be replaced
    """
    text = ""
    with open(filename, "r", encoding="utf-8") as f:
        line = f.readline()
        while (line):
            text += line
            if search_string in line:
                text += new_string
            line = f.readline()

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
