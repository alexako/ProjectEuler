#!/bin/python


if __name__ == '__main__':
    # Sum of multiples of 3 and 5 up to 1000
    print sum([num for num in xrange(1000) if not num % 3 or not num % 5])
