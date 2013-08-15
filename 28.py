#!/bin/python


def spiralGenerator(size):

    num = 1
    skip = 1
    yield num
    while skip <= size - 2:
        for i in xrange(4):
            num += skip
            num += 1
            yield num
        skip += 2


if __name__ == '__main__':
    size = 1001
    print "Answer found: %d" % sum([num for num in spiralGenerator(size)])
