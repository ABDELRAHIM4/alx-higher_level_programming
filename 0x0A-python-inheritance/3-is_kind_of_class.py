#!/usr/bin/python3
""" create function """
def is_kind_of_class(obj, a_class):
    """ Returns True if the object is an instance of"""
    if isinstance (obj, a_class):
        return True
    else:
        """ otherwise False """
        return False
