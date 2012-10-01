#!/usr/bin/python

# Euler Project Problem 40

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.416s
user	0m0.360s
sys	0m0.052s
"""
d = ''.join([str(i) for i in xrange(1,1000000)])
ans = reduce(lambda x,y: x*y, [int(d[(10**e)-1]) for e in xrange(1,7)])
print 'Answer to problem 40:', ans
