#!/usr/bin/python3
def no_c(my_string):

    temp_list = list(my_string)
    temp_lists = []

    for i in temp_list:
        if i != 'c' and i != 'C':
            temp_lists.append(i)

    my_string = ''.join(temp_lists)
    return my_string
