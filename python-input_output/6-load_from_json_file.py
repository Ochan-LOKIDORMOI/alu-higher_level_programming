#!/usr/bin/python3
"""Defines created objects from a json file"""


import json


def load_from_json_file(filename):
    """This is a created objects from json"""
    with open(filename, "r") as f:
        return json.load(f)
