#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()

    t_a1 = tuple_a + (0, 0)
    t_b1 = tuple_b + (0. 0)
    new_tuple = (*new_tuple, t_a1[0] + t_b1[0], t_a1[1] + t_b1[1])

    return (new_tuple)
