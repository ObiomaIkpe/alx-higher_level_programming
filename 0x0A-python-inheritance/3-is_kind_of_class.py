#!/usr/bin/python3

"""Defines a function `is_kind_of_class`"""


def is_kind_of_class(obj, a_class):
    """Checks if @obj is an instance of @a_class, or @a_class is a
    superclass of @obj class.

    Args:
        obj: object to be checked
        a_class: specified class

    Return:
        True if @obj is an instance of, or is an instance of a class
        that was derived from @a_class, otherwise, False
    """
    return (isinstance(obj, a_class))
