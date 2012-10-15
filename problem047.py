#!/usr/bin/python

# Euler Project Problem 47

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.747s
user	0m0.728s
sys	0m0.016s
"""

size = 10**6
n_factor = [0]*size
for n in xrange(2, size):
    if n_factor[n] == 0:
        for k in xrange(2*n, size, n):
            n_factor[k] += 1

goal = [4]*4
for i in xrange(2, size):
    if n_factor[i:i+4] == goal:
        print 'Answer to problem 47:', i
        break
