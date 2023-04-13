#!/usr/bin/python3
"""
    A module that create a function which add two integers
"""


def add_integer(a, b=98):
    """Function that adds two integers"""
    if type(a) not in [int, float]:
        raise TypeError('a should be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b should be an integer')

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
