#!/usr/bin/python3

"""Defines a function, add_attribute"""


def add_attribute(obj, var, value):
    """This function is equivalent to obj.var = value

    Args:
        obj (object): object to be modified
        var (any): the variable to be added as attribute
        value (any): the value to be assigned to the variables.
    Raises:
        TypeError: if attribute can't be created
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, var, value)
