import random, math
from numpy import matrix,array

def get_primes(n):
    """Generate primes < n. Algorithm: Sieve of Eratosthenes."""

    if n <= 2:
        return []

    sieve = range(3, n, 2)
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0]*-((bottom-top)//si)
    return [2] + [el for el in sieve if el]

def get_sieve(n):
    """Generate the Sieve of Eratosthenes."""
    sieve = [True]*n
    sieve[0] = sieve[1] = False
    for p in xrange(2, n):
        if sieve[p]:
            for i in xrange(2*p, n, p):
                sieve[i] = False
    return sieve

 
_mrpt_num_trials = 5 # number of bases to test
 
def is_probable_prime(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    return True
 

def prim_pyth_trips(max=None):
  '''generate all primative triples such that 
  the sum is less than or equal to max'''
  u=matrix( [[1,2,2], [-2,-1,-2], [2,2,3]] )
  a=matrix( [[1,2,2], [2,1,2], [2,2,3]] )
  d=matrix( [[-1,-2,-2], [2,1,2], [2,2,3]] )
  m=[ array([3,4,5]) ]
  while m:
    for i in m:
      yield i
    g=( (i*j).getA1() for i in m for j in (u,a,d) )
    m=[ i for i in g if max is None or sum(i)<=max ]

def pyth_trips(max):
  '''generate all triples such that 
  the sum is less than or equal to max'''
  for i in prim_pyth_trips(max):
    ret=i[:]
    while sum(ret)<=max:
      yield ret
      ret=ret+i

def get_proper_divisors(N):
    divisors = set([1])
    for n in xrange(2, int(math.sqrt(N))+1):
        if N%n == 0:
            divisors.add(n)
            divisors.add(N/n)
    divisors = list(divisors)
    divisors.sort()
    
    return divisors

def get_prime_factors(N, primes):
    prime_factors = []
    for p in primes:
        k = 0
        while N%p == 0:
            k += 1
            N /= p
        if k != 0:
            prime_factors.append((p, k))
        if N == 1:
            break
    return prime_factors
