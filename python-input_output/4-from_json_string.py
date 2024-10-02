#!/usr/bin/python3
"""module json"""
import json

"""function that returns an object to be represented by a JSON string"""


def from_json_string(my_str):
    """
    args:
    my_str: object to represented as json

    Return:
    data
    """
    data = json.loads(my_str)
    return data
