#!/usr/bin/python3
"""json module"""

import json

"""Function that writes an Object to a text file,
using a JSON representation:"""


def save_to_json_file(my_obj, filename):
    """
    args:
    my_obj: objecte to pass  a json
    filename: name of the file to create
    """

    with open(filename, 'w') as my_file:
        data = my_file.write(json.dumps(my_obj))
