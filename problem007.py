#!/usr/bin/python

# Euler Project Problem 7

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.150s
user    0m0.136s
sys 0m0.012s
"""

# The number of primes up to n is pi(n) ~= n/ln(n)
# Because pi(2*10^5) > 10001 will a sieve with 2*10^5 values be enough.

sieve = [True for i in xrange(int(2e5))]
cnt = 0
for i in xrange(2, len(sieve)):
    if sieve[i]:
        cnt += 1
        if cnt == 10001:
            P = i
            break
        for j in xrange(2*i, len(sieve), i):
            sieve[j] = False

print 'Answer to problem 7:', P
