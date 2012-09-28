#!/usr/bin/python

# Euler Project Problem 98

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.748s
user	0m0.736s
sys	0m0.008s
"""
import math

f = open('data/words.txt','r')
line = f.readline()
f.close()

# Sort by length.
words = [x.strip('\"') for x in line.split(',')]
words.sort(cmp=lambda x, y: len(x)-len(y))

# Algorithm
# Find all word anagrams through comparing equal length words.
# Calculate the maximum length of these.
# Calculate the squares with digit length up to the maximum length of 
# anagrams.
# For each anagram map try to map a square with digit and letter lengths
# equal.
# Check that the mapping is correct, i.e. bijective.
# Map the anagram pair with the mapping to get the other number.
# Check that the number doesn't have leading zeros.
# Check that the number is an integer square.
# Save the largest square.


max_len = max(map(len, words))
len_index = [[-1, -1] for _ in xrange((max_len+1))]
i = 0
for w in words:
    if len_index[len(w)][0] == -1:
        len_index[len(w)][0] = i
    len_index[len(w)][1] = i+1
    i += 1

anagrams = []
for L in xrange(1, max_len+1):
    if len_index[L][0] == -1:
        continue
    for i in xrange(len_index[L][0], len_index[L][1]):
        for j in xrange(i+1, len_index[L][1]):
            w1 = list(words[i])
            w2 = list(words[j])
            w1.sort()
            w2.sort()
            if w1 == w2:
                anagrams.append((words[i], words[j]))

max_len = max(map(lambda x: len(x[0]), anagrams))
int_ceil = lambda x: int(math.ceil(x))
N = int_ceil((10**(float(max_len)/2)))
squares = [x*x for x in xrange(0, N+1)]
ans = 0
for (w1, w2) in anagrams:
    start =int(10**(float(len(w1)-1)/2))
    end = int_ceil(10**(float(len(w1))/2))
    for i in xrange(start, end+1):
        if len(str(squares[i])) != len(w1):
            continue
        mapping = {k : v for (k, v) in zip(w1, str(squares[i]))}
        if len(set(mapping.values())) != len(set(mapping.keys())):
            # Not bijective.
            continue
        w = ''.join([mapping[x] for x in w2])
        if w[0] == '0':
            # Leading zero.
            continue
        n = int(w)
        if math.sqrt(n) == int(math.sqrt(n)):
            ans = max(n, squares[i], ans)

print 'Problem 98 answer:', ans
