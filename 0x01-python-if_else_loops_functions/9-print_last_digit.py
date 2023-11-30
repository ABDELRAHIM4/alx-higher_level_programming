#!/usr/bin/python3
def print_last_digit(number):
    last_digit = str(number)[-1]
    if last_digit == '-':
        return '0'
    else:
        return last_digit
