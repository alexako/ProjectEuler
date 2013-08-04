#!/bin/python


def divisorSum(num):
    return sum([n for n in xrange(1, num/2 + 1) if not num % n])


def amicablePair(limit):

    pairs = dict((n, divisorSum(n)) for n in xrange(1, limit))    

    return sum([num for num in xrange(1, limit) if pairs.get(pairs[num], 0) == num and pairs[num] != num])


if __name__ == '__main__':
    limit = 10000
    print "Answer found: ", amicablePair(limit)
