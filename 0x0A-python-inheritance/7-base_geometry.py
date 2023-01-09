#!/usr/bin/python3

"""Creates a class BaseGeometry"""


class BaseGeometry:
    """Defines an object based on based on 6-base_geometry.py"""

    def area(self):
        """Raises an Exception with message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks and validates @value

        Args:
            name (str): name as string
            value (int): value to be checked

        Raises:
            TypeError: if @value is not an integer
        """
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
