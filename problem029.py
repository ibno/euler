#!/usr/bin/python

# Euler Project Problem 29

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.053s
user    0m0.048s
sys 0m0.004s
"""

uniques = set(a**b for a in xrange(2, 101) for b in xrange(2, 101))
res = len(uniques)
print 'Answer to problem 29:', res
