#!/usr/bin/python

# Euler Project Problem 48

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.044s
user	0m0.036s
sys	0m0.004s
"""

print 'Answer to problem 48:',sum([x**x for x in xrange(1,1001)])%10**10
