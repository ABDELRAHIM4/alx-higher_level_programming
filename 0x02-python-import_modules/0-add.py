#!/usr/bin/python3
def add(a, b):
    from add_0 import add
    return add(a, b)

a = 1
b = 2

print(f"{a} + {b} = {add(a, b)}")
