#!/usr/bin/python

# Euler Project Problem 3
import math

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.372s
user    0m0.352s
sys 0m0.016s
"""

# Test all primes from 2 to square root of 600851475143 (N) if they divide N.
# For every prime divide N with this prime number until there's a reminder or 
# the result is 1.
# If the result is 1 the last prime is the greatest prime factor.
# If there's a reminder continue dividing with the next prime number.

L = 0
N = 600851475143
sieve = [True for i in xrange(int(math.sqrt(N)))]
sieve[0] = sieve[1] = False
for i in xrange(len(sieve)):
    if sieve[i]:
        while N%i == 0:
            N/=i
        if N == 1:
            # Largest factor found
            L = i
            break
        for k in xrange(2*i, int(math.sqrt(N)), i):
            sieve[k] = False

print 'Problem 3 answer:', L
