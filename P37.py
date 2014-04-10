# -*- coding: utf-8 -*-
#==============================================================================
# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly
# we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable
# from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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

PMax = 1000001
PList = np.ones(PMax)
PList[1] = 0
ii = 2
while (ii*ii < PMax):
    if PList[ii]:
#        print 'Testing', ii
        jj = 2*ii
        while jj < PMax:
            PList[jj] = 0
            jj += ii
    ii += 1

Primes = []
for ii in range(1,PMax):
    if PList[ii]:
        Primes.append(ii)


def isTrunc(Prime):
    sPrime = str(Prime)
    nlen = len(sPrime)
    try:
        for nn in range(1,nlen):
#            print Prime, 'testing', sPrime[nn:], sPrime[:-nn]
            Primes.index(int(sPrime[nn:]))
            Primes.index(int(sPrime[:-nn]))
    except:
        return False
    return True

idx = 5
ntot = 0
nsum = 0

print 'Finding Trunc'

while ntot < 11:
    if isTrunc(Primes[idx]):
        print '***WINNER***', Primes[idx]
        ntot += 1
        nsum += Primes[idx]
    idx += 1

print nsum
# 748317