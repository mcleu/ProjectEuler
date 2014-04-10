# -*- coding: utf-8 -*-
#==============================================================================
# We shall say that an n-digit number is pandigital if it makes
# use of all the digits 1 to n exactly once. For example, 2143
# is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?
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

def isPandi(number):
    snum = str(number)
    nlen = len(snum)
#    print snum, nlen
    try:
        for nn in range(1,nlen+1):
#            print 'testing', nn
            snum.index(str(nn))
    except:
        return False
    return True

# 1+2+3+4 = 10 and  1+2+3+4+5+6+7 = 28.
# The only Padi that is not divisible by 3 are 4 and 7 digits long.
PMax = 7654321
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

print 'Prime list Done!'

for ii in range(PMax-1, 1, -1):
    if PList[ii]:
        if isPandi(ii):
            print ii
            break

# 7652413