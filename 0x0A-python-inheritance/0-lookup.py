#!/usr/bin/python3

"""Defines a function `lookup`"""


def lookup(obj):
    """Searches @obj for all it attributes.

    Args:
        obj (object): An instance of any type class.

    Returns:
        List of available attributes and methods of @obj.
    """
    field = obj.__dict__
    """ for name in obj:
        fields += [name]

    """
    return (dir(obj))
