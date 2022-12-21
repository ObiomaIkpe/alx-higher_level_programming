#!/usr/bin/python3

"""Creates a class Square."""


class Square:
    """Defines a square by (1-square.py)."""

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size (int): size of square
        """
        self.__size = self.__set_x(size)

    def __set_x(self, size):
        """Setter function to assign self.__size.

        Args:
        size (int): size of square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

        return (self.__size)
