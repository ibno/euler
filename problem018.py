#!/usr/bin/python

# Euler Project Problem 18

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.028s
user    0m0.020s
sys 0m0.004s
"""

s = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def max_route(triangle, i, depth, max_depth, lookup):

    if lookup[i] != -1:
        return lookup[i]

    if depth == max_depth:
        return triangle[i]

    left = max_route(triangle, i+depth, depth+1, max_depth, lookup)
    right = max_route(triangle, i+depth+1, depth+1, max_depth, lookup)

    lookup[i] = triangle[i] + max([left, right])
    return lookup[i]

triangle = map(int, s.split())
lookup = [-1]*len(triangle)
S = max_route(triangle, 0, 1, 15, lookup)
print 'Answer to problem 18:', S
