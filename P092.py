# -*- coding: utf-8 -*-
#==============================================================================
# A number chain is created by continuously adding the square of the digits
# in a number to form a new number until it has been seen before.
#
# For example,
#
# 44 -> 32 -> 13 -> 10 -> 1 -> 1
# 85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
#
# Therefore any chain that arrives at 1 or 89 will become stuck in
# an endless loop. What is most amazing is that EVERY starting
# number will eventually arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?
#==============================================================================


import numpy as np

def sq89(num):
    dsum = sqnum(num)
    if dsum == 89:
        return True
    elif dsum == 1:
        return False
    else:
        return sq89(dsum)

def sqnum(num):
    snum = str(num)
    dsum = 0
    for digit in snum:
        dsum += int(digit)**2
    return dsum

mask = np.zeros(600)
for ii in range(1,600):
    mask[ii] = sq89(ii)

sum89 = 0
for ii in range(1,10000000):
#    if (ii%10000==0):
#        print ii
    sum89 += mask[sqnum(ii)]

print sum89
#8581146