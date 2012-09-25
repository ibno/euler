#!/usr/bin/python

# Euler Project Problem 31

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m0.051s
user	0m0.040s
sys	0m0.008s
"""

def count_combinations(left, coin_pool, lookup):
    """Try to match the left amount with the different coins. Count all
    combinations. Store the values in a lookup table for speed increase."""

    if left == 0:
        # A match. 
        return 1

    if coin_pool == []:
        # Couldn't be matched, don't count this one.
        return 0

    if lookup[coin_pool[0]][left] != -1:
        return lookup[coin_pool[0]][left]
    

    k = left/coin_pool[0]
    lookup[coin_pool[0]][left] = 0
    for v in xrange(k+1):
        lookup[coin_pool[0]][left] += count_combinations(left-v*coin_pool[0],\
                                                        coin_pool[1:], lookup)

    return lookup[coin_pool[0]][left]

coins = [1, 2, 5, 10, 20, 50, 100, 200]
lookup = { coin_value : [-1]*201 for coin_value in coins}
S = count_combinations(200, coins, lookup)
print 'Problem 31 answer:', S
