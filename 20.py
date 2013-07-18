#!/bin/python


def get_factorial(num):

    factorial = 1
    for n in range(2, num+1):
        factorial *= n - 1
    return factorial


def get_sum_of_digits(num):
    return sum([int(n) for n in str(num)])

if __name__ == '__main__':
    print "Answer found: ", get_sum_of_digits(get_factorial(100))
