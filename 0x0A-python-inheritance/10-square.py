#!/usr/bin/python3
""" a class that inherits from BaseGeometry"""
class BaseGeometry:
    """ create BaseGeometry class """
    def area(self):
        """ area method """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ integer_validator method """
        self.name = name
        self.value = value
        if  type(value) != int:
            raise TypeError(f"{self.name}  must be an integer")
        elif value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry """
    def __init__(self, width, height):
        self.integer_validator("width",width)
        self.integer_validator("height",height)
        self.__width = height
        self.__height = width
    def area(self):
        """area method """
        return self.__width * self.__height
    def __str__(self):
        """ __str__ method """
        return "[Rectangle]{}/{}" .format(self.__size,self.__size)
class Square(Rectangle):
    """ Class Square that inherits from Rectangle"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size",size)
        self.__size = size
    def area(self):
        """area() method """
        return self.__size* self.__size
