#!/usr/bin/env python3
def no_c(my_string):
    if my_string == None:
        return None
    else:
        result = ''
        for char in my_string:
            if char != 'c' and char != 'C':
                result += char
        return result
