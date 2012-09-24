#!/usr/bin/python

# Euler Project Problem 17

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.029s
user    0m0.024s
sys 0m0.000s
"""

        
lookup = { 1 : 'one',\
           2 : 'two',\
           3 : 'three',\
           4 : 'four',\
           5 : 'five',\
           6 : 'six',\
           7 : 'seven',\
           8 : 'eight',\
           9 : 'nine',\
           10 : 'ten',\
           11 : 'eleven',\
           12 : 'twelve',\
           13 : 'thirteen',\
           14 : 'fourteen',\
           15 : 'fifteen',\
           16 : 'sixteen',\
           17 : 'seventeen',\
           18 : 'eighteen',\
           19 : 'nineteen',\
           20 : 'twenty',\
           30 : 'thirty',\
           40 : 'forty',\
           50 : 'fifty',\
           60 : 'sixty',\
           70 : 'seventy',\
           80 : 'eighty',\
           90 : 'ninety',\
           1000 : 'onethousand'}

cnt = 0
for n in xrange(1, 1001, 1):
    s = ''
    if n in lookup:
        s += lookup[n]
    else:
        hundreds = n/100
        if hundreds != 0:
            s += lookup[hundreds]+'hundred'
        if (n%100) != 0:
            if n/100 != 0:
                s += 'and'
            if (n%100) in lookup:
                s += lookup[n%100]
            else:
                tens = ((n%100)/10)*10
                ones = n%10
                s += lookup[tens]+lookup[ones]
    cnt += len(s)

print 'Problem 17 answer:', cnt 
