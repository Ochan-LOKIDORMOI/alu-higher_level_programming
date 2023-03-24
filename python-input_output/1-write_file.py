#!/usr/bin/python3
"""This writes a file"""


def write_file(filename="", text=""):
    """Written file"""
    with open(filename, 'w+') as f:
        return f.write(text)
