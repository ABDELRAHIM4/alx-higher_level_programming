#!/usr/bin/python3
""" create function """
def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class"""
    if type(obj) is a_class:
        return True
    else:
        """ otherwise False. """
        return False
