#!/usr/bin/python

# Euler Project Problem 6

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.025s
user    0m0.012s
sys 0m0.016s
"""

n = 100
# O(n) solution
#R = sum([x for x in xrange(1, n+1)])**2 - sum([x*x for x in xrange(1, n+1)])

# O(1) solution
# Because :
# (1 + 2 + ... + n)^2 = n^2 * (n+1)^2 * 1/4
# 1^2 + 2^2 + ... + n^2 = n * (n+1) * (2n+1) * 1/6

R = n**2 * (n+1)**2 / 4 - n* (n+1) * (2*n+1) / 6

print 'Answer to problem 6:', R
