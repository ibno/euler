#!/usr/bin/python

# Euler Project Problem 4

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.345s
user    0m0.336s
sys 0m0.012s
"""

# Converting to string is actually faster than arithmetic reversing.
L = 0
for A in xrange(100, 1000, 1):
    for B in xrange(A, 1000, 1):
        if str(A*B) == str(A*B)[::-1] and A*B > L:
            L = A*B

print 'Answer to problem 4:', L
