#!/usr/bin/python

# Euler Project Problem 2

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.025s
user    0m0.020s
sys 0m0.000s
"""

a = 1
b = 1
S = 0
# Fibonacci sequence: 
# F(0) = F(1) = 1 
# F(i) = F(i-1) + F(i-2), i >= 2
while a <= 4e6:
    if a%2 == 0:
        S += a
    c = a
    a = b
    b += c

print 'Answer to problem 2:', S
