#!/usr/bin/python3

"""Returns the list of available attributes and methods of an object"""


def lookup(obj):
    # temp_list is the return
    temp_list = []

    for value in dir(obj):
        temp_list.append(value)

    return temp_list
