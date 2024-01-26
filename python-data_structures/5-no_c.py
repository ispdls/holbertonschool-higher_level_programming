#!/usr/bin/python3
def no_c(my_string):
    new_string = ""

    for count in range(len(my_string)):
        if my_string[count] != 'c' and my_string[count] != 'C':
            new_string = new_string + my_string[count:(count + 1)]

    return (new_string)
