#!/usr/bin/python3
"""son module"""
import json

"""function that creates an Object from a “JSON file”:"""


def load_from_json_file(filename):
    """
    args:
    filename: name of file

    Return:
    Object
    """
    with open(filename, 'r', encoding='utf-8') as my_file:
        return json.load(my_file)
