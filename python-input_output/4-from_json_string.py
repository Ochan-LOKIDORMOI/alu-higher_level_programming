#!/usr/bin/python3
"""Defines from json string to object"""


import json


def from_json_string(my_str):
    """This is json string to object"""
    return json.loads(my_str)
