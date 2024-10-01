#!/usr/bin/python3

"""function to read a file utf-8"""


def read_file(filename=""):
    """open the file to read"""    
    with open(filename, "r") as myfile:
        print(myfile.read())
