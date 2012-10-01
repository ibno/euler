#!/usr/bin/python

# Euler Project Problem 5
import fractions

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.043s
user    0m0.032s
sys 0m0.008s
"""

def lcm(a, b):
    """Return lowest common multiple."""
    return a*b/fractions.gcd(a, b)

# Get prime factors for each number from 2 to 20. 

L = 1
for x in xrange(2,21):
    L = lcm(L,x)

print 'Answer to problem 5:', L
