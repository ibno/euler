#!/usr/bin/python

# Euler Project Problem 10

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m1.526s
user    0m1.504s
sys 0m0.016s
"""

sieve = [True for i in xrange(2*10**6)]

S = 0
for i in xrange(2, len(sieve)):
    if (sieve[i]):
        S += i
        for j in xrange(2*i, len(sieve), i):
            sieve[j] = False


print 'Problem 10 answer:', S
