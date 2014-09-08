#!/bin/bash/python

from itertools import permutations


DIV = [2, 3, 5, 7, 11, 13, 17]

def hasProperty(num):
    for i in xrange(1, len(DIV)+1):
        if (int(num[i] + num[i+1] + num[i+2]) % DIV[i-1] != 0):
            return False
    return True

def get_pandigitals(list):
    return [''.join(x) for x in permutations(list) if len(str(int(''.join(x)))) == 10]


if __name__ == '__main__':
    pans = get_pandigitals("1234567890")
    pan_sum = []

    for i in pans:
        if hasProperty(''.join(i)):
            pan_sum.append(int(i))

    if pan_sum: print "Answer found: %d" % sum(pan_sum)
