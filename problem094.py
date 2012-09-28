#!/usr/bin/python

# Euler Project Problem 94 

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
"""
from eulertools import prim_pyth_trips

ans = 0
for (a,b,c) in prim_pyth_trips(10**9):
    a_tmp = min(a, b)
    b = max(a, b)
    a = a_tmp
    if 2*a == c+1:
        ans += a+b+c

print 'Problem 94 answer:', ans
