#!/bin/python


def isPrime(num):
    for i in range(2, num):
        if num % i:
            return False
    return True


def getCycleLength(num):
    """ Fermat's little theorem """

    count = 1
    if not num % 2: return getCycleLength(num/2)
    if not num % 5: return getCycleLength(num/5)
    while (pow(10, count) - 1) % num != 0:
        count += 1

    return count

if __name__ == '__main__':

    longest = 0
    length = 0

    for i in xrange(1, 1000):
        if not isPrime(i):
            length = getCycleLength(i)
            if length > longest:
                longest = length
                answer = i

        print "%d: %d digit recurring cycle" % (i, length)

    print "Answer found: %d" % answer
