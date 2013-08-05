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


def getAbundants(num):
    yield [n for n in xrange(12, num) if factorSum(n)]


def getAbundantSums(nums, limit):

    sums = []
    for i in nums:
        for j in nums:
            n = i + j
            if n < limit:
                sums.append(n)

    return set(sorted(sums))

if __name__ == '__main__':
    limit = 28123
    limit += 1

    abundants = [num for num in getAbundants(limit)]
    sums = getAbundantSums(abundants[0], limit)

    print "Answer found: ", sum([num for num in xrange(1, limit) if num not in sums])
