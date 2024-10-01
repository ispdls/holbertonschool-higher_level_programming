#!/usr/bin/python3
"""impoet json module"""
import json

"""function that returns the JSON representation of an object (string):"""


def to_json_string(my_obj):
    """"
    args:
    my_obj: The object to convert to JSON format.

    return:
    data:  A string containing the JSON representation of the object.
    """

    data = json.dumps(my_obj)
    return data
