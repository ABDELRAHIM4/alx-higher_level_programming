#!/usr/bin/python3
"""
This module defines a rectangle object
"""
class Rectangle:
    """
    rectangle object with getter and setter
    """
    def __init__(self,width = 0,height = 0):
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
    def area(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * self.__height
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 *(self.__width + self.__height)
