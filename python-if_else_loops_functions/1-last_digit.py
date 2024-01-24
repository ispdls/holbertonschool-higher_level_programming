#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_num = abs(number) % 10

if number < 0:
    last_num = -last_num


if last_num > 5:
    print("Last digit of {} is {} end is greater than 5".format(number, last_num))

elif last_num == 0:
    print("Last digit of {} is {} and is 0".format(number, last_num))

elif last_num < 6 and last_num != 0:
    print("Last digit of {} is {} end is less than 6 and not 0".format(number, last_num))
