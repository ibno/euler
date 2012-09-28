#!/usr/bin/python

# Euler Project Problem 35

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m1.175s
user	0m1.156s
sys	0m0.016s
"""
import eulertools
from math import ceil, log10

sieve = eulertools.get_sieve(10**6)
rotate = lambda x, n: (x-(x/10**(n-1))*10**(n-1))*10 + x/10**(n-1)

c = 0
for p in xrange(2, 10**6):
    n = i = int(ceil(log10(p)))
    while sieve[p] and i > 0:
        p = rotate(p, n)
        i -= 1

    if i == 0:
        c += 1

print 'Problem 35 answer:', c
