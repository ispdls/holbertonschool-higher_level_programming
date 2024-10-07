#!/usr/bin/python3
"""returns the dictionary description with simple data structure(list,
dictionary, string, integer and boolean) for JSON serialization of an object"""


def class_to_json(obj):
    """
    argv:
    obj
    
    Return:
    temp_dict
    """
    if not hasattr(obj, __dict__):
        return {}

    temp_dict = {}

    for k, v in obj.__dict__.items():
        if isinstance(v, (list, dict, bool, str, int)):
            temp_dict[k] = v

    return temp_dict
