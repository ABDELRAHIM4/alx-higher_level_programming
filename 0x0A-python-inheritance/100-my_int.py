#!/usr/bin/python3
""" Creating a class that inherits from int"""
class MyInt:
    """ Create a class MyInt """
    def __init__(self, value):
        """__init__ method"""
        self.value = value

    def __eq__(self, other):
        """__eq__ method """
        if isinstance(other, MyInt):
            return self.value != other.value
        elif isinstance(other, int):
            return self.value != other
        else:
            return NotImplemented

    def __ne__(self, other):
        """ __ne__ method """
        if isinstance(other, MyInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __repr__(self):
        """ __repr__ method """
        return f"MyInt({self.value})"
