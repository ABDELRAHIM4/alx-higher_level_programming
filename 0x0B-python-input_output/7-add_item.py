#!/usr/bin/python3
""" Adds all arguments to a Python list, and then save them to a file """
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_item(args):
    """ Adds all arguments to a Python list, and then save them to a file"""
    items = load_from_json_file('add_item.json')
    items.extend(args)
    save_to_json_file('add_item.json', items)

if __name__ == '__main__':
    add_item(sys.argv[1:])
