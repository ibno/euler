#!/usr/bin/python

# Euler Project Problem 39

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.053s
user	0m0.040s
sys	0m0.012s
"""

triples = [[] for _ in xrange(1001)]
for u in xrange(1, 100):
    for v in xrange(1, 100):
        a = u*u + 2*u*v
        b = 2*v*v + 2*u*v
        c = u*u + 2*v*v + 2*u*v
        for k in xrange(1,100):
            l = [k*a, k*b, k*c]
            if sum(l) > 1000:
                break
            l.sort()
            if l not in triples[sum(l)]:
                triples[sum(l)].append(l)

p = map(len, triples)
print 'Answer to problem 39:', p.index(max(p))
