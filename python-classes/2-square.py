#!/usr/bin/python3
# 1-square.py
"""Define a class Square."""


class Square:

    """Private instance attribute: size"""
    def __init__(self, size=0):

        """Initialises of size"""
        self.__size = size

        # Validate if size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Validate if size is non zero
        if size < 0:
            raise TypeError("size must be >= 0")
