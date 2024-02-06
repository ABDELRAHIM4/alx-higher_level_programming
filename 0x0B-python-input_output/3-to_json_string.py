#!/usr/bin/python3
"""  JSON representation of an object (string) """
import json

def to_json_string(my_obj):
    """  JSON representation of an object (string)"""
    json_string = json.dumps(my_obj)
    return json_string
