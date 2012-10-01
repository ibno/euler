#!/usr/bin/python

# Euler Project Problem 38

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.126s
user	0m0.124s
sys	0m0.000s
"""

for n in xrange(10000):
    digits_str = ''
    for k in xrange(1,10):
        digits_str += str(k*n)
        if len(digits_str) >= 9:
            break
    d = int(digits_str)
    digits = map(int, digits_str)
    digits.sort()
    if digits == range(1,10):
        res = d

print 'Answer to problem 38:', res
