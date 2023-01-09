#!/usr/bin/python3

"""Creates a class Square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines an object which is a subclass of `Rectangle`"""

    def __init__(self, size):
        """Initializes the square.

        Args:
            size (int): size of square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the string representation of the object"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
