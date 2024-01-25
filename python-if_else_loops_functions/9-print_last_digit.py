#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        temp = abs(number) % 10
    else:
        temp = abs(number) % 10 * -1

    print(temp, end='')
    return temp
