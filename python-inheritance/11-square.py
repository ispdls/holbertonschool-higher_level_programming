#!/usr/bin/python3
"""
This module defines classes related to basic geometry.

Classes:
    Rectangle: Base class.
    Square: Class inherits Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size):
        """Instantiation of class"""
        super().integer_validator('size', size)

        self.__size = size

    def area(self,):
        """Returns area
        """
        return self.__size * self.__size

    def __str__(self):
        """string object"""
        return "[Square] {}/{}".format(self.__size, self.__size)
