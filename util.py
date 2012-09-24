
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
