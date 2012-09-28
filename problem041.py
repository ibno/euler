#!/usr/bin/python

# Euler Project Problem 41

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.028s
user	0m0.028s
sys	0m0.000s
"""

from eulertools import is_probable_prime
from itertools import permutations

for p in reversed([int(''.join(n)) for n in permutations('1234567')]):
    if is_probable_prime(p):
        ans = p
        break
print 'Problem 41 answer:', ans
