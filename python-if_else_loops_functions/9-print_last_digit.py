#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        temp = abs(number) % 10
    else:
        temp = abs(number) % 10

    print(temp, end='')
    return temp
