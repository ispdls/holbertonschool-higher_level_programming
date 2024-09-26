#!/usr/bin/python3
"""function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """"
    args:
        obj: The object to check.
        a_class: The class to compare with.

    True if the object is an instance of a class that inherited (directly
    or indirectly) from the specified class ; otherwise False.
    """

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True

    else:
        return False
