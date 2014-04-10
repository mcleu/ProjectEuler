# -*- coding: utf-8 -*-
#===============================================================================
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025  385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.
#===============================================================================

import time

def diffSosqSqos(n):
    sosq = sum([i**2 for i in range(1,n+1)]) # Sum of Squares
    sqos = sum(range(1,n+1))**2 # Square of Sums

    return abs(sosq-sqos)
    
st=time.time()
print diffSosqSqos(10)
print diffSosqSqos(100)
print time.time() - st