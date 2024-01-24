#!/usr/bin/python3
for letter in range(ord('a'), ord('z') + 1):
    if letter == ord('e') or letter == ord('q'):
        continue
    print("{}".format(chr(letter)), end='')
