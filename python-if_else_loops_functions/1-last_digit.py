#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = number % 10
if number < 0:
    last_number *= -1
if last_number > 5:
    print(f"Last digit of {number} is {last_number} and is greater than 5")
if last_number < 6:
    print(f"Last digit of {number} is {last_number} and is less than 6 and not 0" ) 
if last_number == 0:
    print(f"Last digit of {number} is {last_number} and is 0" )
