#!/usr/bin/python3
"""
This module defines a rectangle object
"""
class Rectangle:
    """ definition a class rectangle """
    def __init__(self, width=0, height=0):
         """initializing a rectangle """
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        """ set the width of rectangle """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        """ set the height of rectangle """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value
