#!/usr/bin/python

# Euler Project Problem 22

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.048s
user    0m0.048s
sys 0m0.000s
"""

f = open('data/names.txt','r')
line = f.readline()
f.close()

names = [x.strip('\"') for x in line.split(',')]
names.sort()

res = 0
for i in xrange(len(names)):
    res += sum(map(lambda x: x-ord('A')+1, map(ord, names[i])))*(i+1)

print 'Answer to problem 22:', res
