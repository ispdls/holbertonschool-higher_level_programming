#!/usr/bin/python3
"""module sys to use argv"""
import sys

"""calling the funtion seve to json fike and load from json file"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""the file name"""
file_name = 'add_item.json'

save_to_json_file(sys.argv[1:], file_name)

load_list = load_from_json_file(file_name)
