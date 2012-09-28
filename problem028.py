#!/usr/bin/python

# Euler Project Problem 28

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.030s
user    0m0.024s
sys 0m0.004s
"""

def spiral_sum(i, ply, max_size):

    if 2*ply+1 > max_size:
        return 0

    SE = i+(2*ply)
    SW = i+2*(2*ply)
    NW = i+3*(2*ply)
    NE = i+4*(2*ply)

    return SE+SW+NW+NE+spiral_sum(NE, ply+1, max_size)

S = 1+spiral_sum(1, 1, 1001)
print 'Problem 28 answer:', S
