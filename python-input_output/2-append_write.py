#!/usr/bin/python3

"""Function the append a string to a file and return the len """


def append_write(filename="", text=""):
    """open the filename to append the string in text"""
    with open(filename, 'a') as myfile:
        myfile.write(text)

    return len(text)
