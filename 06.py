#!/bin/python


def sum_of_squares(num):
    return sum([i*i for i in range(num+1)])


def square_of_sum(num):
    total = sum([i for i in range(num+1)])
    return total * total

if __name__ == '__main__':
    print square_of_sum(100) - sum_of_squares(100)
