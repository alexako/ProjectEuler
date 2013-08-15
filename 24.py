#!/bin/python


import itertools


def permutations(n, target):

    total = len(n)
    list = itertools.permutations(n, total)

    for count, perm in enumerate(list, start=1):
        if count == target:
            return ''.join(perm)


if __name__ == '__main__':

    nums = '0123456789'
    target = 1000000

    print "Answer found: ", permutations(nums, target)
