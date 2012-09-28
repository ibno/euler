#!/usr/bin/python

# Euler Project Problem 32

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.844s
user	0m0.792s
sys	0m0.044s
"""

import itertools

pandigitals = [x for x in itertools.permutations(range(1, 10))]
products = set()
for p in pandigitals:
    c = p[0]*(1000*p[1] + 100*p[2] + 10*p[3] + p[4])
    d = (10*p[0] + p[1])*(100*p[2] + 10*p[3] + p[4])
    ab = 1000*p[5] + 100*p[6] + 10*p[7] + p[8]
    if c == ab or d == ab:
        products.add(ab)

print 'Problem 32 answer:',sum(products)
