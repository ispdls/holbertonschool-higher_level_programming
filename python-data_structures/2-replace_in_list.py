#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    index = 0

    if idx < 0 or idx >= len(my_list):
        return my_list

    else:
        for value in my_list:
            if index == idx:
                my_list[idx] = element

            index += 1
        return my_list
