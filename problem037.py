#!/usr/bin/python

# Euler Project Problem 37

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.761s
user	0m0.736s
sys	0m0.024s
"""
from eulertools import get_sieve, get_primes

sieve  = get_sieve(10**6)
primes = get_primes(10**6)
del primes[0:4]

res = 0
for p in primes:
    for i in xrange(0, len(str(p))):
        if not sieve[int(str(p)[i:])]:
            truncatable_prime = False
            break
        if not sieve[int(str(p)[:i+1])]:
            truncatable_prime = False
            break
        truncatable_prime = True
    if truncatable_prime:
        res += p

print 'Answer to problem 37:', res
