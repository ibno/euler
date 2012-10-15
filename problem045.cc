/* problem45.cc */
#include <iostream>

typedef unsigned long long uint64;

using namespace std;

inline uint64 T(uint64 n) { return (n*(n+1))/2; }

inline uint64 P(uint64 n) { return (n*(3*n-1))/2; }

inline uint64 H(uint64 n) { return n*(2*n-1); }

struct map {
    uint64 first;
    uint64 second;
    uint64 value;
};

int main()
{

    /* Problem 45
     * Benchmark
     * Intel Core2 Duo CPU P8400  @ 2.26GHz 
     * real	0m21.448s
     * user	0m21.437s
     * sys	0m0.000s
     * */
    uint64 Pi, Hj, Hi, Tj, i, j, index, ph_size, ht_size;
    uint64 limit = 100000;
    uint64 lookup_size = 1000000;

    map *lookupPH = new map[lookup_size];
    map *lookupHT = new map[lookup_size];

    index = 0;
    for (i = 1; i < limit; ++i) {
        Pi = P(i);
        for (j = 1; j < limit; ++j) {
            Hj = H(j);
            if (Hj > Pi) {
                break;
            }
            if (Pi == Hj) {
                lookupPH[index].first = i;
                lookupPH[index].second = j;
                lookupPH[index].value = Pi;
                index++;
            }
        }
    }

    ph_size = index;

    index = 0;
    for (i = 1; i < limit; ++i) {
        Hi = H(i);
        for (j = 1; j < limit; ++j) {
            Tj = T(j);
            if (Tj > Hi) {
                break;
            }
            if (Hi == Tj) {
                lookupHT[index].first= i;
                lookupHT[index].second = j;
                lookupHT[index].value = Hi;
                index++;
            }
        }
    }

    ht_size = index;

    for (i = 0; i < ph_size; ++i) {
        for (j = 0; j < ht_size; ++j) {
            if (lookupPH[i].value == lookupHT[j].value) {
                if (lookupPH[i].value == 1 || lookupPH[i].value == 40755) 
                    continue;
                cout << "Answer to problem 45: " << lookupPH[i].value << endl;
                return 0;
            }
        }
    }

    delete lookupPH;
    delete lookupHT;

    return 0;
}

