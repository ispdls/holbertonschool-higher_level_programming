#!/usr/bin/python3

""" function that returns True if the object is exactly an
instance of the specified class ; otherwise False"""


def is_same_class(obj, a_class):

    """ Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns: True if the object is exactly an instance of the class.
    """

    if type(obj) is a_class:
        return True
    else:
        return False
