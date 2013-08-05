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


def abundants(num):
    yield [n for n in xrange(12, num) if factorSum(n)]


if __name__ == '__main__':
    limit = 28123
    limit += 1

    a = [num for num in abundants(limit)]
    abunds = [num1 - num2 for num2 in xrange(1, limit) for num1 in a[0]]
    print "Answer found: ", sum(abunds)
