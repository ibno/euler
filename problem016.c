/* problem016.c */

#include <stdio.h>

#define POWER (1000)
#define SET_BIT(x, n) ((x)[((n)/32)]|=(1<<((n)%32)))

typedef unsigned uint32;
typedef unsigned long long uint64;

uint32 number[(POWER)/32+1];


int main(int argc, char **argv)
{
	/* Benchmark 
	 * Intel Core2 Duo CPU P8400  @ 2.26GHz 
	 * -O3 on gcc version 4.6.3
	 * real	0m0.001s
	 * user	0m0.000s
	 * sys	0m0.000s
	 * */

	uint64 numerator;
	uint32 quotient;	
	uint32 remainder;
	int i, sum = 0;

	SET_BIT(number, POWER);
	while (1) {
		for (i = POWER/32 + 1; i >= 0; --i)
			if (number[i] != 0) {
				remainder = 0;
				for (; i >= 0; --i) {
					numerator = (uint64)number[i] + (((uint64)remainder)<<32);
					quotient = (int)(numerator/10);
					number[i] = quotient;
					remainder = numerator%10;
				}
				/* The last digit is in the remainder. */
				sum += remainder;
			} else if (i == 0) {
				printf("Answer to problem 16: %d\n", sum);
				return 0;
			}
	}
}

