#!/usr/bin/python3
"""Defines a function, `write_file`"""


def write_file(filename="", text=""):
    """Writes content of @text into @filename file

    Args"
        filename (str): file to be editted
        text (str): content to be written into @filename
    """
    try:
        with open(filename, "x", encoding="utf-8") as f:
            ret = f.write(text)
    except FileExistsError:
        with open(filename, "w", encoding="utf-8") as f:
            ret = f.write(text)

    return (ret)
