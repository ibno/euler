#!/usr/bin/python

# Euler Project Problem 14

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m2.907s
user    0m2.888s
sys 0m0.012s
"""

# Use dynamic programming by storing chain lengths for starting values in a 
# lookup table.
LOOKUP_SIZE = 10**6
lookup = [0]*LOOKUP_SIZE

longest_chain_start = 0
longest_chain = 0
start_value = 1
while start_value < 10**6:
    n = start_value
    if n >= LOOKUP_SIZE or lookup[n] == 0:
        chain_len = 0
        chain = [n]
        while n != 1:
            if n%2 == 0:
                n /= 2
            else:
                n = 3*n + 1

            if n < LOOKUP_SIZE and lookup[n] != 0:
                chain_len += lookup[n]
                n = 1
            else:
                chain.append(n)
                chain_len += 1

        for i in xrange(len(chain)):
            if chain[i] < LOOKUP_SIZE:
                lookup[chain[i]] = chain_len-i+1

        if chain_len > longest_chain:
            longest_chain = chain_len
            longest_chain_start = start_value
    start_value += 1

print 'Problem 14 answer:', longest_chain_start
