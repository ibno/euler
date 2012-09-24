#!/usr/bin/python

import math

# Euler Project Problem 20

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.030s
user    0m0.012s
sys 0m0.016s
"""

S = sum(map(int, str(math.factorial(100))))
print 'Problem 20 answer:', S
