#!/usr/bin/python

# Euler Project Problem 44

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m8.585s
user	0m8.573s
sys	0m0.000s
"""
import math

isqrt = lambda x: int(math.sqrt(x))

K = [(k*(3*k-1))/2 for k in xrange(1, 10000)]
J = [(j*(3*j-1))/2 for j in xrange(1, 10000)]
for Pk in K:
    for Pj in J:
        l = Pk + Pj
        i = Pk - Pj
        if l < 0 or i < 0:
            continue
        if isqrt(1+24*l)**2 == (1+24*l) and (1+isqrt(1+24*l))%6 == 0 and\
           isqrt(1+24*i)**2 == (1+24*i) and (1+isqrt(1+24*i))%6 == 0:
            print 'Answer to problem 44:', abs(i)
            exit()
