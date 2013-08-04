#!bin/python

import math


def generateFactors(num):
    """ Generates factors of an int """
    
    yield 1
    
    limit = int(math.sqrt(num) + 1)
    for i in xrange(2, limit):
        if not num % i:
            yield i
            yield num / i


def factors(num):
    """ Returns unsorted list of factors of an int
            Duplicates may occur when applicable
     """
    return list(generateFactors(num))


def factorSum(num):
    return num < sum(set(factors(num)))


def isAbundant(num):

    for a in xrange(1, num):
        for b in xrange(1, num):
            if factorSum(a) and factorSum(b) and a + b == num:
                return True


if __name__ == '__main__':
    limit = 28123
    limit += 1

    print "Answer found: ", sum([num for num in xrange(12, limit) if not isAbundant(num)])
#    print "Answer found: ", sum([num for num in xrange(1, limit) for a in xrange(num) for b in xrange(num) if factorSum(a) and factorSum(b) and a + b == num])
