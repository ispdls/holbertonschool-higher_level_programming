#!/usr/bin/pyhon3
def no_c(my_string):

    temp_list = list(my_string)

    for i in temp_list:
        if i == 'c' or i == 'C':
            temp_list.remove(i)

    my_string = ''.join(temp_list)
    return my_string
