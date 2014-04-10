# -*- coding: utf-8 -*-
#==============================================================================
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the
# factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#==============================================================================




def fact(number):
    if (number == 1) or (number == 0):
        return 1
    else:
        return number * fact(number - 1)

factlist = [fact(ii) for ii in range(10)]

def factsum(number):
    fsum = 0
    snum = str(number)
    for digit in snum:
        fsum += factlist[int(digit)]
    return fsum

bigsum = 0
for ii in xrange(3,100000): # 9! * 7 == 2540160
    if ii == factsum(ii):
#        print ii
        bigsum += ii

print bigsum
# 40730