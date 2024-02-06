#!/usr/bin/python3
""" create function that returns True if the object is an instance of a class that inherited """
def inherits_from(obj, a_class):
    """ Returns True if the object is an instance of a class that inherited (directly or indirectly) """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
