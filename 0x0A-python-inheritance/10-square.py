#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(value) != int:
            raise TypeError(f"{self.name}  must be an integer")
        elif value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("height",height)
        self.integer_validator("width",width)
        self.__width = height
        self.__height = width
    def area(self):
        return self.__width * self.__height
    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size",size)
        self.__size = size
    def area(self):
        return self.__size* self.__size
    def __str__(self):
        return (f"[Rectangle] {self.__size}/{self.__size}")
