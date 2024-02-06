#!/usr/bin/python3
"""creates an Object from a “JSON file """
import json
def load_from_json_file(filename):
    """creates an Object from a “JSON file """
    with open(filename, 'r') as file:
            data = json.load(file)
            if isinstance(data, dict):
                return data
            elif isinstance(data, list):
                return data
            else:
                raise ValueError("JSON string doesn't represent an object")
