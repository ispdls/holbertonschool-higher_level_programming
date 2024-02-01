#!/usr/bin/python3
def uniq_add(my_list=[]):

    temp_list = set()
    sum_resukt = 0

    for list_num in my_list:
        temp_list.add(list_num)

        sum_resukt += sum(temp_list)
