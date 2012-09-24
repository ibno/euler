#!/usr/bin/python

# Euler Project Problem 21

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.101s
user    0m0.084s
sys 0m0.012s
"""

import math

def d(n):
    res = 1
    for q in xrange(2, int(math.sqrt(n))+1):
        if n%q == 0:
            res += q
            if q != n/q:
                res += n/q

    return res

d_lookup = [0]
for i in xrange(1, 10000):
    d_lookup.append(d(i))

s = 0
for a in xrange(10000):
    b = d_lookup[a]
    if b < 10000 and d_lookup[b] == a:
        if a != b:
            s += a

print 'Problem 21 answer:', s
