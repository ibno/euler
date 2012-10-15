#!/usr/bin/python

# Euler Project Problem 396

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
"""

def base_n(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
        return ((num == 0) and numerals[0]) or (base_n(num // b, b,\
            numerals).lstrip(numerals[0]) + numerals[num % b])

def weak_goodstein_seq(n):
    g = n
    k = 2
    while g != 0:
        yield g
        g = int(str(base_n(g, k)), k+1)-1
        k += 1

n = 1
for k in weak_goodstein_seq(3):
    print n, k
    n += 1
print n-1
