#!/usr/bin/python3
""" Module 3-square: class Square """
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
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return self.__size ** 2
