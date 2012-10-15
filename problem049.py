#!/usr/bin/python

# Euler Project Problem 49

from eulertools import get_primes

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m2.019s
user	0m1.980s
sys	0m0.036s
"""

def is_permutation(p, q):
    p = str(p)
    q = str(q)
    pc = [0]*10
    for c in p:
        pc[int(c)] += 1
    qc = [0]*10
    for c in q:
        qc[int(c)] += 1

    return pc == qc

primes = [p for p in get_primes(10**4) if p > 1000]
for i in xrange(len(primes)):
    for j in xrange(i+1, len(primes)):
        diff = primes[j] - primes[i]
        if is_permutation(primes[i], primes[j]):
            for k in xrange(j+1, len(primes)):
                diff2 = primes[k] - primes[j]
                if diff2 > diff:
                    break
                elif diff2 == diff and is_permutation(primes[j], primes[k]):
                    N = ''.join(map(str, [primes[i], primes[j], primes[k]]))
                    if N == '148748178147':
                        continue
                    print 'Answer to problem 49:', N
                    exit()
