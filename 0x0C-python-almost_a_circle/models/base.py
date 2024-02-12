#!/usr/bin/python3
""" first class Base"""
class Base:
    """ first class Base"""
    """private class attribute __nb_objects = 0"""
    __nb_objects = 0
    """class constructor"""
    def __init__(self, id=None):
        """ class constructor """
        if id != None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
