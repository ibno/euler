#!/usr/bin/python

# Euler Project Problem 33

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.071s
user	0m0.052s
sys	0m0.016s
"""

from fractions import Fraction, gcd

Q = Fraction(1, 1)
for p in xrange(10, 100):
    for q in xrange(p+1, 100):

        if p%10 == 0 and q%10 == 0: 
            # Trivial.
            continue

        if q/10 != 0:
            if p/10 == q%10 and Fraction(p%10, q/10) == Fraction(p, q):
                Q *= Fraction(p, q)
            if p%10 == q%10 and Fraction(p/10, q/10) == Fraction(p, q):
                Q *= Fraction(p, q)
        if q%10 != 0:
            if p%10 == q/10 and Fraction(p/10, q%10) == Fraction(p, q):
                Q *= Fraction(p, q)
            if p/10 == q/10 and Fraction(p%10, q%10) == Fraction(p, q):
                Q *= Fraction(p, q)

            
print 'Problem 33 answer:', Q.denominator
