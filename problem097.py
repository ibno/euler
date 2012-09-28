#!/usr/bin/python

# Euler Project Problem 97

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.029s
user	0m0.024s
sys	0m0.004s
"""

def pow_mod10(a, e, m):
    """Calculates a**e mod m."""
    if e == 0:
        return 1
    if a == 0:
        return 0

    if e%2 == 0:
        return pow_mod10((a*a)%m, e/2, m)
    else: #e%2 == 1:
        return (a*pow_mod10((a*a)%m, e/2, m))%m

ans = (28433*pow_mod10(2, 7830457, 10**10)+1)%10**10
print 'Problem 97 answer:', ans
