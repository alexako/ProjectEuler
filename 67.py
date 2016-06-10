#!/bin/python

def largest_sum(num1, num2, num3):
    if (num2 > num3):
        return num1 + num2
    return num1 + num3

def find_path_of_largest(triangle):
    """ Adding from the bottom up """

    tri = [[int(num) for num in row.split()] for row in triangle.split('\n')]

    for row in xrange(len(tri)-2, 0, -1):
        print row
        for digit in xrange(row):
            tri[row-1][digit] = largest_sum(tri[row-1][digit], tri[row][digit],
                    tri[row][digit+1])

        return tri[0][0]

if __name__=='__main__':

    infile = "67.txt"

    try:
        with open(infile) as inputFileHandle:
            triangle = inputFileHandle.read()
            print "Answer found: ", find_path_of_largest(triangle)
    except IOError:
        print "Error: could not open %s" % infile
