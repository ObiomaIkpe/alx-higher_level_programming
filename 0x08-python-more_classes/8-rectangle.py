#!/usr/bin/python3

"""Creates a class Rectangle"""


class Rectangle:
    """Defines a Rectangle (based on 7-rectangle.py)"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if ((self.__width == 0) or (self.__height == 0)):
            perimeter = 0
        else:
            perimeter = (2 * self.__width) + (2 * self.__height)
        return (perimeter)

    def __str__(self):
        if ((self.__width == 0) or (self.__height == 0)):
            return ("")
        s = []
        for i in range(self.__height):
            for j in range(self.__width):
                s.append(str(self.print_symbol))
            if (i is not range(self.__height)[-1]):
                s.append("\n")

        return ("".join(s))

    def __repr__(self):
        rec = "Rectangle(" + str(self.__width) + ", "
        rec += str(self.__height) + ")"
        return (rec)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_1.area()):
            return (rect_1)
        else:
            return (rect_2)
