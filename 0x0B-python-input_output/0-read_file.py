#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""
def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename,"r",encoding = 'UTF8') as file:
        file.read()
