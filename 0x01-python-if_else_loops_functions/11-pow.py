#!/usr/bin/python3
def pow(a, b):
    if a == 0 and b == 0:
        raise ValueError("0 cannot be raised to the power of 0")

    result = 1
    if b > 0:
        for _ in range(b):
            result *= a
    elif b < 0:
        for _ in range(-b):
            result /= a

    return result
