#!/usr/bin/python3
"""This defines a BaseGeometry class"""


class BaseGeometry:
    """This is a BaseGeomatry class"""

    def area(self):
        """Method not implemented"""
        raise Exception("area() is not implemented")

    def integer_vallidator(self, name, value):
        """This validate a value as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
