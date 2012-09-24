/* problem012.c */
#include <stdio.h>
#include <math.h>



int main(int argc, char **argv)
{

	/* Benchmark
	 * Intel Core2 Duo CPU P8400  @ 2.26GHz with gcc 4.6.3 -03
	 * real	0m0.249s
	 * user	0m0.244s
	 * sys	0m0.004s
	 */
	unsigned T, n, q, div_cnt = 0;

	for (n = 1; div_cnt <= 500 ; ++n) {
		T = n*(n+1)/2;
		div_cnt = 0;
		for (q = 1; q < sqrt(T)+1; ++q) 
			if (T%q == 0)
				div_cnt += 2;
	}

	printf("Problem 12 answer: %d\n", T);
	return 0;
}

