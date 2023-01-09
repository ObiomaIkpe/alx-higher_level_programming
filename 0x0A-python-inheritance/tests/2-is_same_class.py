#!/usr/bin/python3

"""Defines a function, is_same_class"""


def is_same_class(obj, a_class):
    """Checks if @obj is of type @a_class

    Args:
        obj: Object to be compared
        a_class: class to be compared

    Return:
        True if @obj is exactly an instance of a_class otherwise, False
    """
    return (obj.__class__ is a_class)
