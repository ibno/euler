#!/usr/bin/python

# Euler Project Problem 15

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.030s
user    0m0.024s
sys 0m0.004s
"""

# Again dynamic programming with a lookup with the path count stored in each
# cell.

def count_paths(x, y, lookup, dim):
    """DPS of all of paths."""

    if lookup == []:
        for i in xrange(dim):
            lookup.append([0 for j in xrange(dim)])

    if lookup[x][y] != 0:
        return lookup[x][y]

    if x == dim-1 and y == dim-1:
        return 1

    right = 0
    if x != dim-1:
        right = count_paths(x+1, y, lookup, dim)
    down = 0
    if y != dim-1:
        down = count_paths(x, y+1, lookup, dim)

    lookup[x][y] = right+down

    return right+down

S = count_paths(0, 0, [], 21)
print 'Problem 15 answer:', S
