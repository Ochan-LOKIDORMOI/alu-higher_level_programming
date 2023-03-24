#!/usr/bin/python3
"""Defines save object to file"""


import json


def save_to_json_file(my_obj, filename):
    """This is save object to a file"""
    with open(filename, "w+") as f:
        return json.dump(my_obj, f)
