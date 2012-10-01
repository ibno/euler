/* problem097.c */
#include <stdio.h>

typedef unsigned long long uint64;
typedef unsigned uint32;

int main(int argc, char **argv)
{
	uint64 n, x, y, sq, ans;
	uint32 p, b;

	/* Calculate 28433*2^7830457 + 1 
	 * 
	 * real	0m0.002s
	 * user	0m0.000s
	 * sys	0m0.000s
	 * */
	p = 7830457;
	for (b = 1; b < p; b <<= 1);
	for (n = 1; b != 0; b >>= 1) {
		/* Split x into two 5-digit numbers: a and b 
		 * n = 10^5*x + y
		 * n*n = 10^10*x*x + 20^5*x*y + y*y
		 * */
		x = n/100000;
		y = n%100000;
		sq = 200000*x*y + y*y;
		if (p&b) n = (2*sq)%10000000000ull;
	 	else n = sq%10000000000ull;
	}
	ans = (28433*n+1)%10000000000ull;
	printf("Answer to problem 97: %llu\n", ans);
	return 0;
}

