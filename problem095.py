#!/usr/bin/python

# Euler Project Problem 95

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real	0m5.355s
user	0m5.300s
sys	0m0.044s
"""
# sigmas is the sum of proper divisors
N = 10**6
sigmas = [1]*(N+1)
for i in xrange(2, int((N+1)**0.5)):
    for j in xrange(2*i, N+1, i):
        sigmas[j] += i

longest_chain = 0
smallest_member = N
visited = [False]*(N+1)
for i in xrange(2, N+1):
    if visited[i]:
        continue
    n = i
    chain_index = [i]
    chain_len = 0
    is_amicable_chain = False
    while n <= N and not visited[n]:
        visited[n] = True
        n = sigmas[n]
        if n in chain_index:
            is_amicable_chain = True
            chain_index = chain_index[chain_index.index(n):]
            break
        else:
            chain_index.append(n)

    if is_amicable_chain and len(chain_index) > longest_chain:
        longest_chain = len(chain_index)
        smallest_member = min(sigmas[n] for n in chain_index)

print 'Problem 95 answer:', smallest_member
