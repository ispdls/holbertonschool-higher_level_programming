#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    temp_list = []
    temp_list = temp_list + my_list

    if my_list:
        for i in range(len(my_list)):
            if (my_list[i] % 2) == 0:
                temp_list[i] = True
            else:
                temp_list[i] = False

    return (temp_list)
