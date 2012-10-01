#!/usr/bin/python

# Euler Project Problem 25

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.026s
user    0m0.020s
sys 0m0.008s
"""

from math import sqrt, log10

n = int((999 + log10(5)/2)/log10((1+sqrt(5))/2))+1
print 'Answer to problem 25:', n
