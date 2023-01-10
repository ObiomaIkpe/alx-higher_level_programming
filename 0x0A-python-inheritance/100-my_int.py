#!/usr/bin/python3

"""Creates a class MyInt"""


class MyInt(int):
    """Defines an object which is a subclass of `int`"""
    def __eq__(self, other):
        """Attempts to imvert `==` to `!=`"""
        return (self.real != other)

    def __ne__(self, other):
        """Attempts to invert `!=` to `==`"""
        return (self.real == other)
