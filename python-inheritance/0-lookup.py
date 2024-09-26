#!/usr/bin/python3

"""Returns the list of available attributes and methods of an object"""


def lookup(obj):

    # temp_list is the return
    temp_list = []

    for value in dir(obj):

        # temp_list store the attributes and methods
        temp_list.append(value)

    # Return the list
    return temp_list
