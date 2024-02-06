#!/usr/bin/python3
class BaseGeometry:
    """ define a class"""
    def area(self):
        """ raises an Exception with the message area() is not implemente """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
            if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0"""
        self.name = name
        self.value = value
        if  not isinstance (value,int):
            raise TypeError(f"{self.name}  must be an integer")
        elif value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
