#!/usr/bin/python

# Euler Project Problem 16

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real   0m0.028s
user    0m0.024s
sys 0m0.000s
"""

S = sum(map(int, str(2**1000)))
print 'Answer to problem 16:', S
