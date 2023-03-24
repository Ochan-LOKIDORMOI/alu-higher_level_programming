#!/usr/bin/python3
"""Defines append file"""


def append_write(filename="", text=""):
    """This is appended file"""
    with open(filename, 'a+') as f:
        return f.write(text)
