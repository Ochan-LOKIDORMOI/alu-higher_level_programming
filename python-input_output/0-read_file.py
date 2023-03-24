#!/usr/bin/python3
"""Reading a file"""


def append_write(filename="", text=""):
    """This file can be read"""
    with open(filename, 'a+') as f:
        return f.write(text)
