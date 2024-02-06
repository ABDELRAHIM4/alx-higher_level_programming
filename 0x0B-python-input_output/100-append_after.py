#!/usr/bin/python3
""" Inserts a line of text to a file, after each line containing a specific string"""
def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing a specific string
    in a file
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    with open(filename, 'w') as file:
        for line in lines:
            if search_string in line:
                file.write(line)
                file.write(new_string)
            else:
                file.write(line)
