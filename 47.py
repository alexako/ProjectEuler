#!/bin/python


import math


def is_prime(num):
    
    for i in xrange(2, num):
        if not num % i:
            return False
    return True

def has_4_prime_factors(num):

    count = 0

    print "Num: ", num

    for i in xrange(2, num):
        if not num % i and is_prime(i):
            print "Prime factor: ", i
            count += 1
            print "Count: ", count

    return count == 4

def find_consecutive_nums():
    num = 5
    while True:
        if has_4_prime_factors(num) and has_4_prime_factors(num + 1) and has_4_prime_factors(num + 2) and has_4_prime_factors(num + 3):
            return (num, num + 1, num + 2, num + 3)

        num += 1
    

if __name__ == '__main__':
    print "Answer found: ", find_consecutive_nums()
