#!/usr/bin/python

# Euler Project Problem 94 

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.028s
user	0m0.016s
sys	0m0.008s
"""

"""
Pell's equation
x^2 - 3*y^2 = 1

If x_1 and y_1 is a solution:
x_{k+1} = x_1*x_k + n*y_1*y_k
y_{k+1} = x_1*y_k + y_1*x_k
Let b, a and h be the base, hypothenuse and height of a equilateral triangle.
If b = a+1: x = (3*a-1)/2, y = h <=> a = (2*x+1)/3.
If b = a-1: x = (3*a+1)/2, y = h <=> a = (2*x-1)/3.
"""
x1, y1 = 2, 1
n, k, L = 3, 2, 0
xk, yk = x1, y1
ans = 0
M = 10**9 
while L <= M:
    x = x1*xk + n*y1*yk
    y = x1*yk + y1*xk

    if (2*x+1)%3 == 0:
        a = (2*x+1)/3
        b = a+1
    elif (2*x-1)%3 == 0:
        a = (2*x-1)/3
        b = a-1
    h = y
    L = 2*a+b

    if (b*h)%2 == 0 and L <= M:
        ans += L
    xk = x
    yk = y
    k += 1

print 'Answer to problem 94:', ans
