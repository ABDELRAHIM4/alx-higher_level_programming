#!/usr/bin/python3
def read_file(filename=""):
    """function that writes a string to a text file """
    with open(filename,"r",encoding = 'UTF8') as file:
        file.read()
