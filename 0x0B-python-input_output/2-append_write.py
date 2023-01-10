#!/usr/bin/python3
"""Defines a funtion `append_write`"""


def append_write(filename="", text=""):
    """Appends @text to the end of @filename

    Args:
        filename (str): file to be editted
        text (str): text to be appended into @filename

    Returns:
        The number of characters added
    """
    try:
        with open(filename, "x", encoding="utf-8") as f:
            ret = f.write(text)
    except FileExistsError:
        with open(filename, "a", encoding="utf-8") as f:
            ret = f.write(text)

    return (ret)
