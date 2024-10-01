#!/usr/bin/python3

"""Function the writes a string to a file utf-8"""


def write_file(filename="", text=""):
    """open the file to write the string text"""
    with open(filename, 'w') as myfile:
        myfile.write(text)

    """return the len of the string text"""
    return len(text)
