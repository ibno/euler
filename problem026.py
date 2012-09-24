#!/usr/bin/python

# Euler Project Problem 26

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.057s
user    0m0.048s
sys 0m0.008s
"""

from itertools import count


def cycle_length(n):
    remainder = 10
    seen = {}
    for i in count(0): 
        if remainder == 0:
            return 0
        elif remainder in seen:
            return i - seen[remainder]
        seen[remainder] = i
        remainder = 10*(remainder%n)

(n, d)= max((cycle_length(n), n) for n in xrange(1, 1000))
print 'Problem 26 answer:', d
