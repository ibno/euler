#!/usr/bin/python

# Euler Project Problem 104

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.524s
user	0m0.432s
sys	0m0.024s
"""
from eulertools import is_pandigital
 
def first_digits(n):
    t = n * 0.20898764024997873 - 0.34948500216800943
    return int((pow(10, t-int(t) + 8)))

a = 1
b = 1
n = 1
print first_digits(500)
while not is_pandigital(a) or not is_pandigital(first_digits(n)):
    a, b = b, (a + b)%10**9
    n += 1

print 'Answer to problem 104:', n
