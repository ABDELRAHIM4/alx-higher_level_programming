#!/usr/bin/python3
""" Convert an object of a class with simple data structure to a dictionary for JSON serialization """
def class_to_json(obj):
    """ Convert an object of a class with simple data structure to a dictionary for JSON serialization """
    if not isinstance(obj, object):
        raise TypeError("obj must be an instance of a Class")
    result = {}
    for attr, value in vars(obj).items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[attr] = value
        elif isinstance(value, object):
            result[attr] = class_to_json(value)
        else:
            raise ValueError("Unsupported data type: {}".format(type(value)))
    return result
