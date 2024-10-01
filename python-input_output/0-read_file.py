#!/usr/bin/python3
import os

"""function to read a file"""


def read_file(filename=""):
    """open the file to read"""    
    with open(filename, "r", encoding="utf-8") as myfile:
        print(myfile.read())
