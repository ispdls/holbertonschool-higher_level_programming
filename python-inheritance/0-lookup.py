#!/usr/bin/python3

"""Returns the list of available attributes and methods of an object"""


def lookup(obj):

    """Returns the list of available
    attributes and methods of an object"""

    # return obj args
    return dir(obj)
