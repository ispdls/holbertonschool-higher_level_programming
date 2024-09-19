#!/usr/bin/python3
# 1-square.py
"""Define a class Square."""


class Square:

    """Private instance attribute: size"""
    def __init__(self, size=0, position=(0, 0)):

        """Initialises of size"""
        self.__size = size
        self.__position = position

    @property
    # Getter for position
    def position(self):
        return self.__position

    # Difine setter
    @position.setter
    def position(self, value):

        # Setter for position, must be a tuple of 2 positive integers
        if not isinstance(value, tuple) and len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    # Define getter
    @property
    def size(self):
        return self.__size

    # Difine setter
    @size.setter
    def size(self, value):

        # Validate if value is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # Validate if value is non zero
        if value < 0:
            raise TypeError("size must be >= 0")

        # __size is = value
        self.__size = value

    # method that returns the current square area
    def area(self):

        # return the area
        return self.__size * self.__size

    # prints in stdout the square with the character #
    def my_print(self):

        # Print an empty line if size is 0
        if self.__size == 0:
            print("")

        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print('')
