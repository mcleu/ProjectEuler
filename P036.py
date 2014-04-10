# -*- coding: utf-8 -*-
#==============================================================================
# The decimal number, 585 = 10010010012 (binary), is palindromic
# in both bases.
#
# Find the sum of all numbers, less than one million, which are
# palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may
# not include leading zeros.)
#==============================================================================


def isPalin(string):
    return string[::-1]==string


PalinSum = 0

for ii in xrange(1000001):
    if isPalin(str(ii)):
#        print ii
        if isPalin(bin(ii)[2:]):
#            print 'winner', ii
            PalinSum += ii

print PalinSum
# 872187