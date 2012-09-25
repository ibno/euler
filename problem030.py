#!/usr/bin/python

# Euler Project Problem 30

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m5.470s
user	0m5.432s
sys	0m0.032s
"""

res = 0
for n in range(2, 10**6):
    if n == sum([k**5 for k in map(int, str(n))]):
        res += n

print 'Problem 30 answer:', res
