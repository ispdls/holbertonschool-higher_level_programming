#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_num = abs(number) % 10

if number > 0 or last_num == 0:
    print(f"Last digit of {number} is {last_num} ", end="")
else:
    print(f"Last digit of {number} is -{last_num} ", end="")

if last_num > 5 and number > 0:
    print("and is greater than 5")

elif last_num == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
