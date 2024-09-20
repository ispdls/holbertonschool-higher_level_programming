#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Private instance attribute: widht, height"""
    def __init__(self, width=0, height=0):

        """Initialises of width, height"""
        self.__width = width
        self.__height = height

        # Validate if width is an integer
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        # Validate if width is non zero
        if width == 0:
            raise TypeError("width must be >= 0")

        # Validate if height is an integer
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        # Validate if height is non zero
        if height == 0:
            raise TypeError("height must be >= 0")
