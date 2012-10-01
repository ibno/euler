#!/usr/bin/python

# Euler Project Problem 102

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.205s
user	0m0.180s
sys	0m0.020s
"""
from numpy import cross, dot, array
f = open('data/triangles.txt', 'r')
lines = f.read().split()
f.close()

def same_side(u, v, w):
    A = cross(u-v, -v)
    B = cross(u-v, w-v)
    return dot(A, B) >= 0

triangles = [map(int, l.split(',')) for l in lines]
ans = 0
for [u1, u2, v1, v2, w1, w2] in triangles:
    u = array([u1, u2])
    v = array([v1, v2])
    w = array([w1, w2])
    if same_side(u, v, w) and same_side(v, w, u) and same_side(w, u, v):
        # Inside the triangle.
        ans += 1
print 'Answer to problem 102:', ans
