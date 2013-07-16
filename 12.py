#!/bin/python


def nth_triangle_number(nth):
    return sum([i for i in range(nth+1)])


def get_number_of_factors(num):
    quantity = 0
    for i in range(1, int(num/2)+1):
        if not num % i:
            quantity += 1
    return quantity + 1


def get_triangle_number_of(divisors):
    i = 10000
    while get_number_of_factors(nth_triangle_number(i)) <= divisors:
        i += 1

    return nth_triangle_number(i)


if __name__ == '__main__':
    number_of_divisors = 150
    print "Answer found: ", get_triangle_number_of(number_of_divisors)
