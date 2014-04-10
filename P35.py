# -*- coding: utf-8 -*-
#==============================================================================
# The number, 197, is called a circular prime because all rotations of
# the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100:
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?
#==============================================================================


import math
import numpy as np

def isPrime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(math.sqrt(n))+1, 2):
        if n % x == 0:
            return False
    return True

def conEven(string):
    # if it contains an even number it definitly is not a circular prime
    for digit in string:
        if int(digit)%2 == 0:
            return True
    return False

PMax = 1000001
PList = np.ones(PMax)

for ii in range(2,PMax):
    if PList[ii]:
#        print 'Testing', ii
        PList[ii] = isPrime(ii)
        jj = 2*ii
        while jj < PMax:
            PList[jj] = 0
            jj += ii

Primes = []
for ii in range(1,PMax):
    if PList[ii]:
        if not conEven(str(ii)):
#            print ii
            Primes.append(ii)

l1 = [p for p in Primes if p<10]
l2 = [p for p in Primes if p<100 and p>=10]
l3 = [p for p in Primes if p<1000 and p>=100]
l4 = [p for p in Primes if p<10000 and p>=1000]
l5 = [p for p in Primes if p<100000 and p>=10000]
l6 = [p for p in Primes if p<1000000 and p>=100000]

def nextCirc(number, shift=1):
    nstr = str(number)
    return int(nstr[-shift:] + nstr[:-shift])

def isCirc(primes):
    circ = []
    lprimes = len(primes)
    for ii in xrange(lprimes):
        ptest = primes[ii]
        try:
            n = len(str(ptest))
            for nn in range(n):
                p1 = nextCirc(ptest, nn)
                primes.index(p1)

            circ.append(ptest)
        except:
#            pass
            print ptest, 'not circular'
    return circ

ic = isCirc(Primes)

print len(ic)