#!/usr/bin/python3
"""Reading a file."""


def read_file(filename=""):
    """This file can be read"""
    with open(filename) as f:
        line = f.read()
        print(line, end="")
