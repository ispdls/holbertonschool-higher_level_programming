#!/usr/bin/python3
for num in range(0, 10):
    for num1 in range(num + 1, 10):
        if num == 8:
            print("{}{}".format(num, num1),)
            break
        print("{}{}".format(num, num1), end=', ')
