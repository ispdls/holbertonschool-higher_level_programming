#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    temp1 = tuple_a[0] + tuple_b[0]
    temp2 = tuple_a[1] + tuple_b[1]

    temp_tup = (temp1, temp2)

    return temp_tup
