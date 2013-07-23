#!/bin/python


def self_power(num):
    return num**num


if __name__ == '__main__':
    limit = 1000
    sum = 0
    for i in xrange(1, limit + 1):
        sum += self_power(i)

    print "Answer found: ", str(sum)[-10:]
