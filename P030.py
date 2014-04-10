# -*- coding: utf-8 -*-
#==============================================================================
# Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits:
#
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth
# powers of their digits.
#==============================================================================


def S4(n):
    dsum = 0
    nstr = str(int(n))
    for ndigit in nstr:
        dsum += int(ndigit)**4
    return dsum

sum4 = 0

for ii in xrange(2,9500):
    if ii == S4(ii):
        print ii
        sum4 += ii

print 'The sum4 is', sum4



def S5(n):
    dsum = 0
    nstr = str(int(n))
    for ndigit in nstr:
        dsum += int(ndigit)**5
    return dsum

sum5 = 0

for ii in xrange(2,355000):
    if ii == S5(ii):
        print ii
        sum5 += ii

print 'The sum5 is', sum5
