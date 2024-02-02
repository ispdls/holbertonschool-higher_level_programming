#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    temp_keys = sorted(a_dictionary.keys())
    for k in temp_keys:
        v = a_dictionary[k]
        print("{}: {}".format(k, v))
