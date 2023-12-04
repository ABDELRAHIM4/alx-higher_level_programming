#!/usr/bin/env python3
def no_c(my_string):
    if my_string == None:
        return None
    else:
        new_string = my_string.replace('c', '').replace('C', '')
        return new_string
