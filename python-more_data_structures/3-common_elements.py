#!/usr/bin/python3
def common_elements(set_1, set_2):
    temp_list1 = []
    temp_list2 = []

    for list1 in set_1:
        temp_list1.append(list1)

    for list2 in set_2:
        if list2 in temp_list1:
            temp_list2.append(list2)

    return temp_list2    
