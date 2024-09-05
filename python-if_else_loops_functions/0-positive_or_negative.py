#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(F"{number} is positive")
if number == 0:
    print(F"{number} is zero")
if number < 0:
    print(F"{number} is negative")
