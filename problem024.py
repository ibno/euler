#!/usr/bin/python

# Euler Project Problem 24

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m2.302s
user    0m1.780s
sys 0m0.516s
"""

import itertools

permutations = [p for p in itertools.permutations([0,1,2,3,4,5,6,7,8,9])]
permutations.sort()
S = ''.join(map(str, permutations[999999]))
print 'Problem 24 answer:', S 
