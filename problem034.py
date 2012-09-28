#!/usr/bin/python

# Euler Project Problem 34

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.482s
user	0m0.476s
sys	0m0.004s
"""
from math import factorial as fac

c = sum(x for x in xrange(1, 100000) if x == sum(map(fac, map(int, str(x)))))
print 'Problem 34 answer:', c
