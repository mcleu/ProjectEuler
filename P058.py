# -*- coding: utf-8 -*-
#==============================================================================
# Starting with 1 and spiralling anticlockwise in the following way,
# a square spiral with side length 7 is formed.
# 
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
# 
# It is interesting to note that the odd squares lie along
# the bottom right diagonal, but what is more interesting is that
# 8 out of the 13 numbers lying along both diagonals are prime;
# that is, a ratio of 8/13 ≈ 62%.
# 
# If one complete new layer is wrapped around the spiral above,
# a square spiral with side length 9 will be formed.
# If this process is continued, what is the side length of
# the square spiral for which the ratio of primes along both diagonals
# first falls below 10%?
#==============================================================================

import math

# From problem 3
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


# produce numbers along diagonal
n = 1

# Count primes
p = 0
# Total numbers considered
t = 1 # count the center 1 as non prime
for i in range(2,30000,2):
    #print i+1
    for _ in range(4):
        n += i
        if isPrime(n):
            p += 1
    t += 4
    #print double(p)/t
    if double(p)/t < 0.1:
        print '**Winner**', i+1
        break

# 26241
