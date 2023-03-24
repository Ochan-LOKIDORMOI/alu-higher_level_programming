#!/usr/bin/python3
"""Module inherited from the list class"""


class myList(list):
    """A class inherited from list"""
    def print_sorted(self):
        """This print a sorted list"""
        print(sorted(self))
