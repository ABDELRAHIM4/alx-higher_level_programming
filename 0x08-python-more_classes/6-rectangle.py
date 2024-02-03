#!/usr/bin/python3
"""
create a rectangle class
"""
class Rectangle:
    number_of_instances = 0
    """ definition a class rectangle """
    def __init__(self, width=0, height=0):
        """initializing a rectangle """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        """ set the width of rectangle """
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
        """ set the height of rectangle """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
    def area(self):
        """ calculate the area of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * self.__height
    def perimeter(self):
        """calculate the parimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    def __str__(self):
        """ print the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ''
        return '\n'.join(['#' *self.__width] * self.__height)
    def __repr__(self):
        """ print the rectangle usung eval"""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)
    def __del__(self):
        """ print the message when the rectangle is deleted  """
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
