#!/usr/bin/python3
def max_integer(my_list=[]):

    if not my_list:
        return None

    temp_num = my_list[0]
    for i in my_list:

        if i > temp_num:
            temp_num = i

    return temp_num
