#!/usr/bin/python3
""" create a BaseGeometry class """
class BaseGeometry:
    """ create BaseGeometry class """
    def area(self):
        """ area of BaseGeometry """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ checks if value is integer """
        self.name = name
        self.value = value
        if type(value) != int:
            raise TypeError(f"{self.name}  must be an integer")
        elif value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
""" create a Rectangle class """
class Rectangle(BaseGeometry):
    """ create Rectangle class that inherts from BaseGeometry class """
    def __init__(self, width, height):
        """ instantiation with height and width """
        self.integer_validator("height",height)
        self.integer_validator("width",width)
        self.__width = height
        self.__height = width
    def area(self):
        """ area of Rectangle """
        return self.__width * self.__height
    def __str__(self):
        """ str() should return, the Rectangle description """
        return (f"[Rectangle] {self.__width}/{self.__height}")
class Square(Rectangle):
    """ create Square class that inherts from Rectangle class  """
    def __init__(self, size):
        """ Instantiation with size """
        self.integer_validator("size",size)
        self.__size = size
    def area(self):
        """ area() implemented """
        return self.__size* self.__size
    def __str__(self):
        """ str() should return, the square description """
        return (f"[Square] {self.__size}/{self.__size}")
