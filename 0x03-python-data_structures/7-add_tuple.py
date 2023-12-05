#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_tuple = ()

    for i in range(2):
        value_a = tuple_a[i] if i < len(tuple_a) else 0
        value_b = tuple_b[i] if i < len(tuple_b) else 0
        sum_tuple += (value_a + value_b,)

    return sum_tuple
