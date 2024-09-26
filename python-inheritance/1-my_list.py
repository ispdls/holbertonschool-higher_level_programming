#!/usr/bin/python3

"""class Mylist"""


class MyList(list):

    """class initialization"""
    def __init__(self):
        pass

    """ method print_sorted: that prints the list,
    but sorted (ascending sort)"""
    def print_sorted(self,):
        temp_list = sorted(self)
        print(temp_list)
