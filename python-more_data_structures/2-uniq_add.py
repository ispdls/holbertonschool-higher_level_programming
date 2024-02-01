#!/usr/bin/python3
def uniq_add(my_list=[]):

    count = 0
    temp_list = []

    for list_num in my_list:
        if list_num in temp_list:
            continue
        else:
            temp_list.append(list_num)

    for i in temp_list:
        count += i

    return count
