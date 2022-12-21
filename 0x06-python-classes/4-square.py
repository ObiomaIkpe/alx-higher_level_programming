#!/usr/bin/python3

"""Creates a class Square"""


class Square:
    """Defines a square based on '3-square.py'"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size (int): size of new square
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
