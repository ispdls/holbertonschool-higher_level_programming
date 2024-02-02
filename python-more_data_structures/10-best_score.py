#!/usr/bin/python3
def best_score(a_dictionary):
    temp_key = None
    temp_value = 0

    if a_dictionary is None:
        return None

    for k, v in a_dictionary.items():
        if v > temp_value:
            temp_key = k
            temp_value = v

    return temp_key
