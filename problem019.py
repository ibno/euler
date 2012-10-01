#!/usr/bin/python

# Euler Project Problem 19

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.035s
user    0m0.016s
sys 0m0.016s
"""

# Jan 1900 was a Monday and 365%7 = 1 -> 1 Jan 1901 was a Tuesday.

day = 1
year = 1
days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
days_in_months_leap = [31,29,31,30,31,30,31,31,30,31,30,31]

sunday_count = 0
for year in xrange(1, 101):
    # Leap year
    if year%4 == 0 or year == 100:
        for inc in days_in_months_leap:
            day += inc
            day = day%7
            if day == 6:
                sunday_count += 1
    else:
        for inc in days_in_months:
            day += inc
            day = day%7
            if day == 6:
                sunday_count += 1

print 'Answer to problem 19:', sunday_count
