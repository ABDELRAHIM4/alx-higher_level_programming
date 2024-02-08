#!/usr/bin/python3
"""
create a rectangle class
"""
class Rectangle:
    """ create a rectangle class
        class attribute print_symbol
        initialized to #
        Used as symbol for string representation
        Can be any type"""
    number_of_instances = 0
    """  class attribute print_symbol nitialized to #
        Used as symbol for string representation
        Can be any type"""
    print_symbol = "#"
    """ definition a class rectangle """
    def __init__(self, width=0, height=0):
        """initializing a rectangle """
        self.width = width
        self.height = height
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
        total = ''
        if self.width == 0 or self.height == 0:
            return total
        for i in range (self.__height):
            """"class attribute print_symbol:
            Initialized to #
            Used as symbol for string representation
            Can be any type"""
            total += (str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                total += '\n'
        return total

    def __repr__(self):
        """ print the rectangle usung eval"""
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """ print the message when the rectangle is deleted  """
        print('Bye rectangle...')
        """ instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
