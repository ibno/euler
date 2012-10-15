#!/usr/bin/python

# Euler Project Problem 42

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.050s
user	0m0.024s
sys	0m0.004s
"""

f = open('data/words.txt', 'r')
words = [w.strip('\"') for w in f.readline().split(',')]

lookup = [False]*len(words)
n = 1
while (n*(n+1))/2 < len(words):
    lookup[(n*(n+1))/2] = True
    n += 1

ans = 0
for word in words:
    if lookup[sum(map(lambda x: 1+ord(x)-ord('A'), word))]:
        ans += 1

print 'Answer to problem 42:', ans
