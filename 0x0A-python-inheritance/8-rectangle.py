#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if  type(value) != int:
            raise TypeError(f"{self.name}  must be an integer")
        elif value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width",width)
        self.integer_validator("height",height)
        self.__width = height
        self.__height = width
