#!/usr/bin/python3
""" Module 4-square: class Square """
class Square():
    """
        Square: defines a square.
        Attributes:
            size (int): size of square.
        Method:
                __init__ : init of size attribute for each instance.
    """
    def __init__(self, size=0):
        """ Initialization of attributes for instances
            Args:
                size (int): size of the square.
        """
        self.__size = size

    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return self.__size ** 2
