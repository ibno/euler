#!/usr/bin/python

import itertools

# Euler Project Problem 9

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.033s
user    0m0.020s
sys 0m0.008s
"""
#Generate triplets with Euclid's method
# Iterative depth to make it faster.
for D in itertools.count(1):
    for u in xrange(D):
        for v in xrange(D):
            a = u*u + 2*u*v
            b = 2*v*v + 2*u*v
            c = u*u + 2*v*v + 2*u*v
            if a+b+c == 1000:
                print 'Problem 9 answer:', a*b*c
                exit()

