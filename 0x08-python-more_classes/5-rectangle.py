#!/usr/bin/python3
"""
create a rectangle class
"""
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ calculate the area of rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * self.height

    def perimeter(self):
        """calculate the parimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """ print the rectangle """
        if self.width == 0 or self.height == 0:
            return ''
        return '\n'.join(["#" *self.name] * self.hi)

    def __repr__(self):
        """ print the rectangle usung eval"""
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """ delete the ectangle """
        print('Bye rectangle...')
