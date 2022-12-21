#!/usr/bin/python3

""" Creating a square object """


class Square:
    """ Write a class Square that defines a square"""

    class __init__(self, size=0):
        """
        the init method is used for initialization

        @self:
            refers to the object itself
        @size:
            the size of the square, must be +ve
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
