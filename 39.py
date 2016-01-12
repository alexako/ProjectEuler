import math


def isRightTriangle(a, b, c):
    return (a*a + b*b) == (c*c)

def findSides(perimeter):
    solutions = 0
    for a in xrange(perimeter/3, perimeter/2):
        for b in xrange(1, a):
            c = perimeter - a - b
            if isRightTriangle(a, b, c):
                solutions += 1

    return solutions


num_of_solutions = {} #key:number_of_solutions val: perimeter
for p in xrange(1, 1001):
    sides = findSides(p)
    if sides:
        num_of_solutions[sides] = p

print "Done finding solutions!"

#Print num of solutions and find largest
largest = max(num_of_solutions.keys())
print "Perimeter: %d Solutions: %d" % (num_of_solutions[largest], largest)
