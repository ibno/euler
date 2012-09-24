#!/usr/bin/python

# Euler Project Problem 12

import itertools, math

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m7.686s
user    0m7.664s
sys 0m0.012s
"""

# Triangle number: T(n) = (n+1)*(n+2)/2

# Brute force method.
for n in itertools.count(1):
    T = n*(n+1)/2
    div_cnt = 0
    for q in xrange(1, int(math.sqrt(T))+1):
        if T%q == 0:
            div_cnt += 2
    if div_cnt > 500:
        print 'Problem 12 answer:', T
        break

