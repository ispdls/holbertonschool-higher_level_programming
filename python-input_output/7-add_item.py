#!/usr/bin/python3
"""module sys to use argv and module os to check if the file exists"""
import sys
import os

"""calling the funtion seve to json fike and load from json file"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""the file name"""
file_name = 'add_item.json'
"""the obj argvs"""
load_list = []
"""check is the file exists"""
if os.path.exists(file_name):
    load_list = load_from_json_file(file_name)
else:
    load_list = []

"""add the argvs"""
load_list.extend(sys.argv[1:])
"""save the file"""
save_to_json_file(load_list, file_name)
