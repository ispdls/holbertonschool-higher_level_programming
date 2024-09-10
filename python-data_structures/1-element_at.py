#!/usr/bin/python3
def element_at(my_list, idx):
    index = 0

    if idx < 0 :
        return None
    
    elif idx > len(my_list):
        return None
    
    else:
        for value in my_list:
            if index == idx:
                return my_list.pop(idx)
            index += 1
                


my_list = [1, 2, 3, 4, 5]
idx = 4
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
