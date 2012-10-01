#!/usr/bin/python

# Euler Project Problem 23

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m2.340s
user    0m2.328s
sys 0m0.008s
"""
import math

def d(n):
    res = 1
    for q in xrange(2, int(math.sqrt(n))+1):
        if n%q == 0:
            res += q
            if n/q != q:
                res += n/q

    return res

abundants = set(i for i in xrange(1,28124) if d(i) > i)
abundant_sum = lambda x: any(x-a in abundants for a in abundants)
S=sum(i for i in xrange(1,28124) if not abundant_sum(i))

print 'Answer to problem 23:', S
