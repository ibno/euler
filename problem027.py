#!/usr/bin/python

# Euler Project Problem 27
from eulertools import get_primes

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m12.114s
user    0m12.089s
sys 0m0.012s
"""

primes = get_primes(1000)
S = 0
N = 0
for a in xrange(-999, 1000):
    for b in xrange(-999, 1000):
        n = 0
        while n**2+a*n+b in primes:
            n += 1
        if n > N:
            N = n
            S = a*b

print 'Answer to problem 27:', S

