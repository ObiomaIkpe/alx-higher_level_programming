#!/usr/bin/python3

"""Create a class Rectangle which is a subclass of `BaseGeometry`"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Rectangle object"""

    def __init__(self, width, height):
        """Initializes object

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates and returns the are of the Rectangle object"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns the string representation of an object"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
