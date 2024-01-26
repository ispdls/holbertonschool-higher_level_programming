#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argument_count = len(sys.argv) - 1

    if argument_count > 0:
        print(f"{argument_count} arguments:")
        for i in range(1, argument_count + 1):
            print(f"{i}: {sys.argv[i]}")
