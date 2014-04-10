# -*- coding: utf-8 -*-
#==============================================================================
# Euler discovered the remarkable quadratic formula:
#
# n**2 + n + 41
#
# It turns out that the formula will produce 40 primes for the
# consecutive values n = 0 to 39. However, when n = 40,
# 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and
# certainly when n = 41, 41**2 + 41 + 41 is clearly divisible
# by 41.
#
# The incredible formula  n**2 - 79n + 1601 was discovered,
# which produces 80 primes for the consecutive values
# n = 0 to 79. The product of the coefficients,
# -79 and 1601, is -126479.
#
# Considering quadratics of the form:
#
# n**2 + an + b, where |a| < 1000 and |b| < 1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
# Find the product of the coefficients, a and b, for the
# quadratic expression that produces the maximum number of
# primes for consecutive values of n, starting with n = 0.
#==============================================================================

import math
import time

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

t0 = time.time()

nmax = 0
for aa in range(-1000,1001):
    for bb in range(-1000,1001):
        nn = 0
        while isPrime(nn**2 + aa*nn+ bb):
            nn += 1
        if nn > nmax:
            nmax = nn
            print nn, aa, bb

t1 = time.time()

print aa*bb, t1 - t0

#-59231