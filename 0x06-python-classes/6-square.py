#!/usr/bin/python3

"""class square that defines a square"""


class Sqaure:
    """Defines a square based on task 5"""

    def __init(self, size=0, position(0, 0)):
        """initialization

        Args:
            size (int): size of the square
            position (int): 0
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter method for size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter method for self.size

        Args:
            value(int): size of square
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (type(value) is not a tuple or
                len(value) != 2 or
                (not isinstance(value[0], int)) or (value[0] < 0) or
                (not isinstance(value[1], int)) or (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculates the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints out the square with '#'"""
        if (self.size == 0):
            print("")
            return

        [print("") for i in range(self.position[1])]
        for i in range(self.size):
            [print(" ", end="") for j in range(Self.position[0])]
            [print(" ", end="") for j in range(Self.size)]
            print("")
