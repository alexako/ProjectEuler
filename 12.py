#!/bin/python


import math


def nth_triangle_number(nth):
    """ Using the fact that 1 + ... + n = n * (n + 1) / 2 """
    return nth * (nth + 1) / 2


def get_number_of_factors(num):

    limit = math.sqrt(num)
    int_sqrt = int(round(limit))

    if int_sqrt ** 2 == num:
        int_limit = int_sqrt
        quantity = 1
    else:
        int_limit = int(limit) + 1
        quantity = 0

    for i in xrange(1, int_limit):
        if not num % i:
            quantity += 2

    return quantity


def get_triangle_number_of(divisors):
    i = 10000
    while get_number_of_factors(nth_triangle_number(i)) <= divisors:
        i += 1

    return nth_triangle_number(i)


if __name__ == '__main__':
    number_of_divisors = 500
    print "Answer found: ", get_triangle_number_of(number_of_divisors)
