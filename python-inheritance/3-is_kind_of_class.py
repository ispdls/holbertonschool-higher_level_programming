#!/usr/bin/python3
"""
 function that returns True if the object is an instance of, or if
    the object is an instance of a class that inherited
    from, the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    args:
        obj: The object to check.
        a_class: The class to compare with.

    return true is an instance of, or if
    the object is an instance of a class that inherited
    """

    return isinstance(obj, a_class)
