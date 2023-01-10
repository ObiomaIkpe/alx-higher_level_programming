#!/usr/bin/python3
"""Creates a class ``student``"""


class Student:
    """Defines a student object"""
    def __init__(self, first_name, last_name, age):
        """Initializes a student object.

        Args:
            first_name (str): student's first name.
            last_name (str): student's lastname.
            age (int): student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of ``Student`` object"""
        return (self.__dict__)
