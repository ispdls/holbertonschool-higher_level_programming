#!/usr/bin/python3
"""
This module defines classes related to basic geometry.

Classes:
    BaseGeometry: Base class.
    Rectangle: Class inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle."""

    def __init__(self, width, height):
        """Instantiation of class"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self,):
        """Returns area
        """
        return self.__width * self.__height

    def __str__(self):
        """string object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
