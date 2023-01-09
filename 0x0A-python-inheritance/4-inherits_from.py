#!/usr/bin/python3

"""Deines a function ``inherits_from``."""


def inherits_from(obj, a_class):
    """Checks if @obj is an instance of a class that inherited (directly
    of indirectly) from @a_class and not an instance of @a_class itself.

    Args:
        obj: object to be checked.
        a_class: specified class.

    Returns:
        True if the above was met, otherwise False.
    """
    if ((type(obj) is not a_class) and isinstance(obj, a_class)):
        return True
    return False
