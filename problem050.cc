/* problem50.cc */
#include <vector>
#include <iostream>

using namespace std;

void get_primes(vector<int> &primes, vector<bool> &sieve)
{
    sieve[0] = false;
    sieve[1] = false;

    for (size_t i  = 2; i < 1000000; ++i) {
        if (sieve[i]) {
            primes.push_back(i);
            for (size_t j = 2*i; j < 1000000; j += i) {
                sieve[j] = false;
            }
        }
    }
}

int main()
{

    /* Benchmark on Intel Core2 Duo CPU P8400  @ 2.26GHz with g++
     * real	0m0.022s
     * user	0m0.016s
     * sys	0m0.004s
     * */
    vector<bool> sieve(1000000, true);
    vector<int> primes; 

    get_primes(primes, sieve);

    int best = 0;
    int best_prime = 0;
    for (size_t i = 0; i < primes.size(); ++i) {
        int sum = 0;
        int count = 0;
        for (size_t j = i; j < primes.size(); ++j) {
            sum += primes[j];
            ++count;
            if (sum >= 1000000) {
                break;
            }
            if (sieve[sum]) {
                if (count > best) {
                    best = count;
                    best_prime = sum;
                }
            }
        }
    }

    cout << "Answer to problem 50: " << best_prime << endl;

    return 0;
}
