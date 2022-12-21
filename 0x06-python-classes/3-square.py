#!/usr/bin/python3

"""Creates a class Square"""


class Square:
    """Defines a square based on '2-square.py'"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size (int): size of new square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates area of the square"""
        return (self.__size ** 2)
