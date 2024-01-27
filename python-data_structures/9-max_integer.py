#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 0:
        return None

    temp = 0

    for count in my_list:
        if temp < count:
            temp = count
        else:
            continue

    return (temp)
