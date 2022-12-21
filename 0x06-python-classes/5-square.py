#!/usr/bin/python3

"""Creates a class Square"""


class Square:
    """Defines a square based on '4-square'"""

    def __init__(self, size=0):
        """Initializes a new square"""
        self.size = size

    @property
    def size(self):
        """Getter function for 'self.size'"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method for 'self.size'"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints out the square with the character '#'"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            if (i != range(self.size)[-1]):
                print("")
        print("")
