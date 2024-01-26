#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argument_count = len(sys.argv) - 1
    sum = 0

    for i in range(1, argument_count + 1):
        count = int(sys.argv[i])
        sum = sum + count

    print(sum)
