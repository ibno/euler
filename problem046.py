#!/usr/bin/python

# Euler Project Problem 46

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.218s
user	0m0.196s
sys	0m0.020s
"""
from eulertools import get_sieve, get_primes
from math import sqrt

def get_odd_composites(n):
    sieve = get_sieve(n)
    composites = []
    for i in xrange(2, len(sieve)):
        if not sieve[i] and i%2 == 1:
            composites.append(i)
    return composites 

isqrt = lambda x: int(sqrt(x))
primes = get_primes(10000)
composites = get_odd_composites(10000)

for n in composites:
    for p in primes:
        if p > n:
            print 'Answer to problem 46:', n
            exit()
        if isqrt((n-p)/2)**2 == (n-p)/2:
            break


