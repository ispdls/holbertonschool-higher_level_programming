#!/usr/bin/python3
def search_replace(my_list, search, replace):

    temp_list = []

    for num in my_list:
        if num == search:
            num = replace
        temp_list.append(num)

    return temp_list
