#!/usr/bin/python3
"""
create a rectangle class
"""
class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
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
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value

    def area(self):
        """ calculate the area of rectangle """
        if self._width == 0 or self._height == 0:
            return 0
        return self._width * self._height

    def perimeter(self):
        """calculate the parimeter of rectangle"""
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """ print the rectangle """
        if self._width == 0 or self._height == 0:
            return ''
        return '\n'.join([''.join(['#' if j < self._height else ' ' for j in range(self._height)]) for i in range(self._width)])

    def __repr__(self):
        """ print the rectangle usung eval"""
        return 'Rectangle({}, {})'.format(self._width, self._height)

    def __del__(self):
        """ delete the ectangle """
        print('Bye rectangle...')
