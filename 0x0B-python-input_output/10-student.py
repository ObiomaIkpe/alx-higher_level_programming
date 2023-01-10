#!/usr/bin/python3
"""Creates a class ``student``"""


class Student:
    """Defines a student object (based on ``9-student.py``"""
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

    def to_json(self, attrs=None):
        """Returns the dictionary representation of ``Student`` object"""
        if (attrs is None):
            return (self.__dict__)

        if ((type(attrs) != list) or
                not all([type(item) is str for item in attrs])):
            return

        ret = {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return (ret)
