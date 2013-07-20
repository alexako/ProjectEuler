#!/bin/python


def Collatz_sequence(number):

    if not number % 2:
        return number / 2
    else:
        return 3 * number + 1


def find_longest_chain():

    longest_chain = 1
    term_count = 1

    for num in xrange(410011, 1000000):
        index = num
        while num > 1:
            num = sequence(num)
            term_count += 1

        if longest_chain < term_count:
            longest_chain = term_count
            starting = index
            print "starting: ", starting, "longest_chain: ", longest_chain

        term_count = 1

    return starting

if __name__ == '__main__':
    print "Answer found: ", find_longest_chain()
