#!/usr/bin/python

# Euler Project Problem 36

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.660s
user	0m0.644s
sys	0m0.012s
"""
s = sum(x for x in xrange(10**6) \
        if str(x)[::-1] == str(x) and bin(x)[2:][::-1] == bin(x)[2:])

print 'Problem 36 answer:', s
