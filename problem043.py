#!/usr/bin/python

# Euler Project Problem 43

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m5.844s
user	0m5.828s
sys	0m0.008s
"""
import itertools

c = 0
for d in itertools.permutations('0123456789'):
    d = ''.join(d)
    if int(d[1:4])%2 == 0 and  \
        int(d[2:5])%3 == 0 and \
        int(d[3:6])%5 == 0 and \
        int(d[4:7])%7 == 0 and \
        int(d[5:8])%11 == 0 and \
        int(d[6:9])%13 == 0 and \
        int(d[7:10])%17 == 0:
            c += int(d)

print 'Answer to problem 43:', c
        
