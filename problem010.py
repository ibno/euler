#!/usr/bin/python

# Euler Project Problem 10

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m1.303s
user	0m1.280s
sys	0m0.020s
"""

sieve = [True for i in xrange(2*10**6)]

S = 2
for i in xrange(3, len(sieve), 2):
    if (sieve[i]):
        S += i
        for j in xrange(2*i, len(sieve), i):
            sieve[j] = False


print 'Problem 10 answer:', S
