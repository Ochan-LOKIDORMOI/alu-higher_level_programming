#!/usr/bin/python3
"""This checks if object is instance of a class that 
inherited from the specified class or not
"""


def inherits_from(obj, a_class):
    """This will returns true if object is an instance of a class thst inherited from the specified class; otherwise false
    """
    return (issubclass(type(obj, a_class) and type(obj) != a_class))
