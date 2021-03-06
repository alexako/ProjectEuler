#!/bin/python

import math
import random
import sys


def find_route(grid_size):

    limit = grid_size
    moves = ['Right', 'Down']
    path = []
    x = 0
    y = 0

    while True:

        next_move = random.choice(moves)

        if x <= limit and y <= limit:
            if next_move == 'Right':
                y += 1
                path.append(next_move)
            else:
                x += 1
                path.append(next_move)

        if x > limit or y > limit:
            path = []
            x = 0
            y = 0

        if len(path) >= limit * 2:
            if x == limit and y == limit:
                break
            else:
            # Reset if there have been [limit] moves and not at target
                path = []
                x = 0
                y = 0

    return ", ".join(path)


def count_paths():

#    paths = []
#    path_count = 0
#    rep = 0

#    while True:
#        rep += 1
#        path = find_route(size)
#        if path not in paths:

#            sys.stdout.write("\rPath Found: %s \t Path Count: %d " % (path[:len(path)/4], path_count+1))
#            sys.stdout.flush()

#            paths.append(path)
#            path_count += 1

#        if rep >= 1000000000:
#            break

#    return "\n\nPath count: %d\n" % path_count

    # One-liner
    return (math.factorial(size*2)) / (math.factorial(size) * math.factorial(size))

if __name__ == '__main__':
    size = 20
    print count_paths()
