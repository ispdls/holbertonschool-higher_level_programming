#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for number in my_list:
        print("{}".format(number))


num = [1,2,3,4,5]
print_list_integer(num)