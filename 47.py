#!/bin/python


import math

def has_4_prime_factors(num):

    count = 0

    for i in xrange(2, int(round(math.sqrt(num)))):
        print "has_4_prime: ", num, i
        if not num % i:
            for j in xrange(2, int(round(math.sqrt(i)))):
                if not i % j:
                    count += 1
    return count == 2
    
def find_consecutive_nums():
    while True:
        num = 10
        print "find_consec: ", num
        if has_4_prime_factors(num) and has_4_prime_factors(num + 1): # and has_4_prime_factors(num + 2) and has_4_prime_factors(num + 3):
            return num

        num += 1

if __name__ == '__main__':
    print "Answer found: ", find_consecutive_nums()
