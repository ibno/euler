#!/usr/bin/python

# Euler Project Problem 1

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.027s
user    0m0.016s
sys 0m0.008s
"""

print 'Problem 1 answer:', sum(set(xrange(3, 1000, 3)).union(xrange(5, 1000, 5)))
