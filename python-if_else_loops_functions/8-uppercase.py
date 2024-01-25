#!/usr/bin/python3
def uppercase(str):
    for temp in str:
        char_temp = ord(temp)
        if char_temp >= ord('a') and char_temp <= ord('z'):
            char_temp = char_temp - (ord('a') - ord('A'))
        print("{}".format(chr(char_temp)), end='')
    print()
