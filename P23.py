# -*- coding: utf-8 -*-
"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper
divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that
28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is
less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant
numbers is 24. By mathematical analysis, it can be shown that
all integers greater than 28123 can be written as the sum of two
abundant numbers. However, this upper limit cannot be reduced any
further by analysis even though it is known that the greatest number
that cannot be expressed as the sum of two abundant numbers is less
than this limit.

Find the sum of all the positive integers which cannot be written as
the sum of two abundant numbers.
"""
import numpy as np

def SumOfDiv(number):
    DivSum = 1
    for ii in range(2,int(np.sqrt(number)+1)):
#    for ii in range(2,number):
#        print ii
        if (number % ii) == 0:
            DivSum += ii
            if not (number/ii) == ii:
                DivSum += number/ii
#            print 'added', ii, number/ii
    return DivSum

isAbun = []

for ii in range(1,28123):
    if ii<SumOfDiv(ii):
        isAbun.append(ii)
#       print ii

SOTMax = 28125
SumOfTwo = np.ones([SOTMax])
isAbunLen = len(isAbun)
for ii in xrange(isAbunLen):
    for jj in xrange(ii,isAbunLen):
#        print ii,jj
        SOT = isAbun[ii]+isAbun[jj]
        if SOT>=SOTMax:
            break
        SumOfTwo[SOT] = 0

NotSOT = 0
for ii in xrange(SOTMax):
    NotSOT += ii * SumOfTwo[ii]

print NotSOT
# 4179871